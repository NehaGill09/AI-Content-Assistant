from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .services import AIContentService
class GenerateView(APIView):
 permission_classes=[IsAuthenticated]
 def post(self,request):
  topic=request.data.get('topic','').strip()
  if not topic:return Response({'detail':'topic is required'},status=400)
  try:return Response(AIContentService().generate(topic,request.data.get('content_type','blog'),request.data.get('tone','professional')).model_dump())
  except Exception as exc:return Response({'detail':'AI generation failed','error':str(exc)},status=502)
