import hashlib
from django.utils import timezone
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import APIKey

class APIKeyAuthentication(BaseAuthentication):
    keyword = 'Api-Key'
    def authenticate(self, request):
        header = request.headers.get('Authorization', '')
        if not header.startswith(self.keyword + ' '):
            return None
        raw = header.split(' ', 1)[1].strip()
        if not raw:
            raise AuthenticationFailed('Invalid API key')
        digest = hashlib.sha256(raw.encode()).hexdigest()
        try:
            key = APIKey.objects.select_related('user').get(key_hash=digest, revoked_at__isnull=True)
        except APIKey.DoesNotExist:
            raise AuthenticationFailed('Invalid API key')
        key.last_used_at = timezone.now()
        key.save(update_fields=['last_used_at'])
        return (key.user, key)
