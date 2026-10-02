import os
from openai import OpenAI
from pydantic import BaseModel,Field
class GeneratedContent(BaseModel):
 title:str=Field(min_length=1); content:str=Field(min_length=1); seo_keywords:list[str]=[]
class AIContentService:
 def __init__(self): self.client=OpenAI(api_key=os.getenv('OPENAI_API_KEY')); self.model=os.getenv('OPENAI_MODEL','gpt-4.1-mini')
 def generate(self,topic,content_type='blog',tone='professional'):
  r=self.client.beta.chat.completions.parse(model=self.model,messages=[{'role':'system','content':'You are an expert content strategist. Return structured data only.'},{'role':'user','content':f'Create {content_type} content about {topic}. Tone: {tone}. Include title, polished content, and SEO keywords.'}],response_format=GeneratedContent)
  return r.choices[0].message.parsed
