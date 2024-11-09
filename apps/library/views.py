from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from apps.library.models import Library
from apps.library.serializers import LibrarySerializer
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class Pagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100

class LibraryAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    pagination_class = Pagination
