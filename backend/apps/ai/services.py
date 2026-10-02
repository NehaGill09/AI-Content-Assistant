import os
from openai import OpenAI
from pydantic import BaseModel, Field
from .models import AIRequest
from .registry import render_prompt
from .telemetry import Timer

class GeneratedContent(BaseModel):
    title: str = Field(min_length=1)
    content: str = Field(min_length=1)
    seo_keywords: list[str] = []

class AIContentService:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.model = os.getenv('OPENAI_MODEL', 'gpt-4.1-mini')

    def generate(self, topic, content_type='blog', tone='professional', user=None):
        prompt, user_prompt = render_prompt('content.generate', {'topic': topic, 'content_type': content_type, 'tone': tone})
        with Timer() as timer:
            response = self.client.beta.chat.completions.parse(
                model=self.model,
                messages=[{'role': 'system', 'content': prompt.system}, {'role': 'user', 'content': user_prompt}],
                response_format=GeneratedContent,
            )
        usage = response.usage
        AIRequest.objects.create(
            user=user,
            prompt_name=prompt.name,
            prompt_version=prompt.version,
            model=self.model,
            latency_ms=timer.elapsed_ms,
            prompt_tokens=getattr(usage, 'prompt_tokens', 0) or 0,
            completion_tokens=getattr(usage, 'completion_tokens', 0) or 0,
            total_tokens=getattr(usage, 'total_tokens', 0) or 0,
            metadata={'content_type': content_type, 'tone': tone},
        )
        return response.choices[0].message.parsed

    def healthcheck(self):
        if not os.getenv('OPENAI_API_KEY'):
            raise RuntimeError('OPENAI_API_KEY is not configured')
        return True
