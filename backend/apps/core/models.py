from django.conf import settings
from django.db import models
class Workspace(models.Model):
 name=models.CharField(max_length=120); owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='workspaces'); created_at=models.DateTimeField(auto_now_add=True)
class AuditEvent(models.Model):
 actor=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True); action=models.CharField(max_length=120); metadata=models.JSONField(default=dict); created_at=models.DateTimeField(auto_now_add=True)
