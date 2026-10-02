from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .streaming import streaming_response

class StreamGenerateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        topic = str(request.data.get('topic', '')).strip()
        if not topic or len(topic) > 1000:
            return Response({'detail': 'topic is required and must be <= 1000 characters'}, status=400)
        return streaming_response(topic, str(request.data.get('content_type', 'blog'))[:40], str(request.data.get('tone', 'professional'))[:40])
