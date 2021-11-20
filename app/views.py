from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters

from .models import Article
from .serializers import ArticleSerializer

# Create your views here.


class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('title', 'author')
