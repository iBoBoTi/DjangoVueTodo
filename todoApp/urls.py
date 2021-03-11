from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoTaskViewSet

router = DefaultRouter()
router.register('todos', TodoTaskViewSet, basename='todos_api')

urlpatterns = router.urls