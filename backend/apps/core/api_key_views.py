import hashlib
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import APIKey

class APIKeyCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        name = str(request.data.get('name', 'default')).strip()[:120]
        raw = APIKey.generate_raw_key()
        prefix = raw[:12]
        APIKey.objects.create(user=request.user, name=name, prefix=prefix, key_hash=hashlib.sha256(raw.encode()).hexdigest())
        return Response({'name': name, 'prefix': prefix, 'api_key': raw}, status=201)

class APIKeyListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response([{'id': k.id, 'name': k.name, 'prefix': k.prefix, 'revoked': bool(k.revoked_at), 'created_at': k.created_at} for k in request.user.api_keys.order_by('-created_at')])
