from django.test import SimpleTestCase
from .registry import render_prompt

class PromptRegistryTests(SimpleTestCase):
    def test_rendered_prompt_contains_variables(self):
        spec, prompt = render_prompt('content.generate', {'topic': 'AI', 'content_type': 'blog', 'tone': 'professional'})
        self.assertEqual(spec.version, '1.0.0')
        self.assertIn('AI', prompt)
        self.assertIn('professional', prompt)
