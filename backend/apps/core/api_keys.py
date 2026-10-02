import secrets
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

class APIKey(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='api_keys')
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
