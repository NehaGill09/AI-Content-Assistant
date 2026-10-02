from django.db import models
from django.conf import settings

class EvaluationCase(models.Model):
    name = models.CharField(max_length=160)
    prompt_name = models.CharField(max_length=120)
    input_variables = models.JSONField(default=dict)
    expected_criteria = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

class EvaluationRun(models.Model):
    case = models.ForeignKey(EvaluationCase, on_delete=models.CASCADE, related_name='runs')
    prompt_version = models.CharField(max_length=40)
    score = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    feedback = models.TextField(blank=True)
    passed = models.BooleanField(default=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
