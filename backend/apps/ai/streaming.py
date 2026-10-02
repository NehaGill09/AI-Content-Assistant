import json
import os
from django.http import StreamingHttpResponse
from openai import OpenAI
from .registry import render_prompt


def stream_content(topic, content_type='blog', tone='professional'):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    prompt, user_prompt = render_prompt('content.generate', {'topic': topic, 'content_type': content_type, 'tone': tone})
    response = client.chat.completions.create(
        model=os.getenv('OPENAI_MODEL', 'gpt-4.1-mini'),
        messages=[{'role':'system','content':prompt.system},{'role':'user','content':user_prompt}],
        stream=True,
    )
    for chunk in response:
        delta = chunk.choices[0].delta.content if chunk.choices else None
        if delta:
            yield f"data: {json.dumps({'delta': delta})}\n\n"
    yield 'data: [DONE]\n\n'


def streaming_response(topic, content_type='blog', tone='professional'):
    return StreamingHttpResponse(stream_content(topic, content_type, tone), content_type='text/event-stream', headers={'Cache-Control':'no-cache','X-Accel-Buffering':'no'})
