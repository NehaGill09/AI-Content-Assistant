from celery import shared_task

@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=True, max_retries=3)
def warmup_ai_provider(self):
    from .services import AIContentService
    AIContentService().healthcheck()
    return {'status': 'ok'}
