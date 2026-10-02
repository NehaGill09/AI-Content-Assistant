from django.conf import settings
from django.db import models

class PromptTemplate(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True)
    active_version = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PromptVersion(models.Model):
    template = models.ForeignKey(PromptTemplate, on_delete=models.CASCADE, related_name='versions')
    version = models.PositiveIntegerField()
    system_prompt = models.TextField()
    user_template = models.TextField()
    model = models.CharField(max_length=120, default='gpt-4.1-mini')
    temperature = models.FloatField(default=0.2)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['template', 'version'], name='uniq_prompt_version')]

class AIRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    prompt_name = models.CharField(max_length=120)
    prompt_version = models.CharField(max_length=40, default='1.0.0')
    model = models.CharField(max_length=120)
    latency_ms = models.PositiveIntegerField(default=0)
    prompt_tokens = models.PositiveIntegerField(default=0)
    completion_tokens = models.PositiveIntegerField(default=0)
    total_tokens = models.PositiveIntegerField(default=0)
    estimated_cost_usd = models.DecimalField(max_digits=12, decimal_places=8, default=0)
    status = models.CharField(max_length=20, default='success')
    metadata = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
