from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.content.views import ContentViewSet
from apps.ai.views import GenerateView
from apps.ai.views_stream import StreamGenerateView
from apps.ai.views_analytics import UsageSummaryView
from apps.ai.health import health
from apps.ai.rag_views import KnowledgeDocumentCreateView
from apps.ai.eval_views import EvaluationRunView
from apps.core.api_key_views import APIKeyCreateView, APIKeyListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
router=DefaultRouter(); router.register('content',ContentViewSet,basename='content')
urlpatterns=[path('health/',health),path('api/',include(router.urls)),path('api/ai/generate/',GenerateView.as_view()),path('api/ai/stream/',StreamGenerateView.as_view()),path('api/ai/usage/',UsageSummaryView.as_view()),path('api/ai/knowledge/',KnowledgeDocumentCreateView.as_view()),path('api/ai/evals/<int:case_id>/run/',EvaluationRunView.as_view()),path('api/auth/token/',TokenObtainPairView.as_view()),path('api/auth/token/refresh/',TokenRefreshView.as_view()),path('api/auth/api-keys/',APIKeyListView.as_view()),path('api/auth/api-keys/create/',APIKeyCreateView.as_view())]
