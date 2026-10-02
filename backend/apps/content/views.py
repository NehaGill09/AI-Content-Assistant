from rest_framework import permissions,viewsets
from .models import ContentDocument
from .serializers import ContentDocumentSerializer
class ContentViewSet(viewsets.ModelViewSet):
 serializer_class=ContentDocumentSerializer; permission_classes=[permissions.IsAuthenticated]
 def get_queryset(self): return ContentDocument.objects.filter(author=self.request.user).prefetch_related('versions')
 def perform_create(self,serializer): serializer.save(author=self.request.user)
