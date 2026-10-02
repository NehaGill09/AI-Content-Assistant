from django.urls import include,path
from rest_framework.routers import DefaultRouter
from apps.content.views import ContentViewSet
from apps.ai.views import GenerateView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
router=DefaultRouter(); router.register('content',ContentViewSet,basename='content')
urlpatterns=[path('api/',include(router.urls)),path('api/ai/generate/',GenerateView.as_view()),path('api/auth/token/',TokenObtainPairView.as_view()),path('api/auth/token/refresh/',TokenRefreshView.as_view())]
