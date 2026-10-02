from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import KnowledgeDocument
from .rag_tasks import index_knowledge_document

class KnowledgeDocumentCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        workspace_id = request.data.get('workspace_id')
        name = str(request.data.get('name', '')).strip()
        content = str(request.data.get('content', '')).strip()
        if not workspace_id or not name or not content:
            return Response({'detail': 'workspace_id, name and content are required'}, status=400)
        document = KnowledgeDocument.objects.create(workspace_id=workspace_id, name=name, content=content)
        index_knowledge_document.delay(document.id)
        return Response({'id': document.id, 'status': 'indexing'}, status=202)
