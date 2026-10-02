from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .services import AIContentService

class GenerateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        topic = str(request.data.get('topic', '')).strip()
        if not topic or len(topic) > 1000:
            return Response({'detail': 'topic is required and must be <= 1000 characters'}, status=400)
        content_type = str(request.data.get('content_type', 'blog'))[:40]
        tone = str(request.data.get('tone', 'professional'))[:40]
        try:
            result = AIContentService().generate(topic, content_type, tone, request.user)
            return Response(result.model_dump())
        except Exception:
            return Response({'detail': 'AI generation failed'}, status=502)
