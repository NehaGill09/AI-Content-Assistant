from celery import shared_task

@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=True, max_retries=3)
def index_knowledge_document(self, document_id):
    from .models import KnowledgeDocument
    from .rag import RAGService
    document = KnowledgeDocument.objects.get(pk=document_id)
    return {'chunks': RAGService().index_document(document)}
