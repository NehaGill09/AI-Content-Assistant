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


class KnowledgeDocument(models.Model):
    workspace = models.ForeignKey('core.Workspace', on_delete=models.CASCADE, related_name='knowledge_documents')
    name = models.CharField(max_length=240)
    content = models.TextField()
    indexed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class DocumentChunk(models.Model):
    document = models.ForeignKey(KnowledgeDocument, on_delete=models.CASCADE, related_name='chunks')
    position = models.PositiveIntegerField()
    content = models.TextField()
    embedding = models.VectorField(dimensions=1536)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['document', 'position'], name='uniq_document_chunk')]

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
