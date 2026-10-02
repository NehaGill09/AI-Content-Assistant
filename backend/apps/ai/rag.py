from django.db import transaction
from pgvector.django import CosineDistance
from .models import KnowledgeDocument, DocumentChunk
from openai import OpenAI
import os

class RAGService:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.embedding_model = os.getenv('OPENAI_EMBEDDING_MODEL', 'text-embedding-3-small')

    def embed(self, text: str) -> list[float]:
        response = self.client.embeddings.create(model=self.embedding_model, input=text)
        return response.data[0].embedding

    @transaction.atomic
    def index_document(self, document: KnowledgeDocument) -> int:
        DocumentChunk.objects.filter(document=document).delete()
        chunks = [document.content[i:i + 1800] for i in range(0, len(document.content), 1800)]
        for index, chunk in enumerate(chunks):
            DocumentChunk.objects.create(document=document, position=index, content=chunk, embedding=self.embed(chunk))
        document.indexed = True
        document.save(update_fields=['indexed', 'updated_at'])
        return len(chunks)

    def retrieve(self, workspace_id, query: str, limit: int = 5):
        vector = self.embed(query)
        return list(DocumentChunk.objects.filter(document__workspace_id=workspace_id, document__indexed=True).annotate(distance=CosineDistance('embedding', vector)).order_by('distance')[:limit])
