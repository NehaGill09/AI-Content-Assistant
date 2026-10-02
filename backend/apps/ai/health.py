from django.http import JsonResponse
from django.db import connection
from django.core.cache import cache

def health(request):
    checks = {}
    try:
        connection.ensure_connection()
        checks['database'] = 'ok'
    except Exception:
        checks['database'] = 'error'
    try:
        cache.set('healthcheck', 'ok', 5)
        checks['redis'] = 'ok'
    except Exception:
        checks['redis'] = 'error'
    ok = all(value == 'ok' for value in checks.values())
    return JsonResponse({'status': 'ok' if ok else 'degraded', 'checks': checks}, status=200 if ok else 503)
