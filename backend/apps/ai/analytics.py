from django.db.models import Avg, Sum, Count
from .models import AIRequest

def usage_summary(user):
    qs = AIRequest.objects.filter(user=user)
    return qs.aggregate(requests=Count('id'), total_tokens=Sum('total_tokens'), average_latency_ms=Avg('latency_ms'), estimated_cost_usd=Sum('estimated_cost_usd'))
