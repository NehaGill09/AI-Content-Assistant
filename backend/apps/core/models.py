from django.conf import settings
from django.db import models
from django.utils import timezone
import secrets

class Workspace(models.Model):
    name = models.CharField(max_length=120)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='workspaces')
    created_at = models.DateTimeField(auto_now_add=True)

class AuditEvent(models.Model):
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=120)
    metadata = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

class APIKey(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='api_keys')
    name = models.CharField(max_length=120)
    prefix = models.CharField(max_length=12, unique=True)
    key_hash = models.CharField(max_length=128, unique=True)
    last_used_at = models.DateTimeField(null=True, blank=True)
    revoked_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def generate_raw_key():
        return 'aca_' + secrets.token_urlsafe(32)

    def revoke(self):
        self.revoked_at = timezone.now()
        self.save(update_fields=['revoked_at'])
