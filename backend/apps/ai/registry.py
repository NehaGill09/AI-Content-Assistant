from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class PromptSpec:
    name: str
    version: str
    system: str
    user_template: str

PROMPTS = {
    'content.generate': PromptSpec(
        name='content.generate', version='1.0.0',
        system='You are an expert content strategist. Produce accurate, useful, audience-aware content. Return structured data only.',
        user_template='Create {content_type} content about {topic}. Tone: {tone}. Include a compelling title, polished content, and SEO keywords.'
    )
}

def render_prompt(name: str, variables: dict[str, Any]) -> tuple[PromptSpec, str]:
    spec = PROMPTS[name]
    return spec, spec.user_template.format(**variables)
