from .models import EvaluationCase, EvaluationRun
from .services import AIContentService

class EvaluationService:
    def run_case(self, case: EvaluationCase, user=None):
        result = AIContentService().generate(user= user, **case.input_variables)
        text = f'{result.title}\n{result.content}'
        criteria = [str(c).lower() for c in case.expected_criteria]
        matched = sum(1 for c in criteria if c in text.lower())
        score = (matched / len(criteria)) if criteria else 1.0
        return EvaluationRun.objects.create(case=case, prompt_version='1.0.0', score=score, passed=score >= 0.8, feedback=f'{matched}/{len(criteria)} criteria matched', created_by=user)
