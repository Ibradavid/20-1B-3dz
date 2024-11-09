from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.library.views import LibraryAPI

router = DefaultRouter()
router.register('api_Library', LibraryAPI, basename='api-Library')

urlpatterns = [
    
]

urlpatterns += router.urls