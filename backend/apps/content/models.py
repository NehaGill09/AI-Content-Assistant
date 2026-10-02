from django.conf import settings
from django.db import models
from apps.core.models import Workspace
class ContentDocument(models.Model):
 workspace=models.ForeignKey(Workspace,on_delete=models.CASCADE,related_name='documents'); author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE); title=models.CharField(max_length=240); content=models.TextField(blank=True); content_type=models.CharField(max_length=40,default='blog'); tone=models.CharField(max_length=40,default='professional'); metadata=models.JSONField(default=dict); version=models.PositiveIntegerField(default=1); created_at=models.DateTimeField(auto_now_add=True); updated_at=models.DateTimeField(auto_now=True)
class ContentVersion(models.Model):
 document=models.ForeignKey(ContentDocument,on_delete=models.CASCADE,related_name='versions'); version=models.PositiveIntegerField(); content=models.TextField(); prompt_snapshot=models.JSONField(default=dict); created_at=models.DateTimeField(auto_now_add=True)
 class Meta: unique_together=[('document','version')]
