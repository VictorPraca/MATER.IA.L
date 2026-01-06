from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EngenheiroViewSet

router = DefaultRouter()
router.register(r'engenheiros', EngenheiroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]