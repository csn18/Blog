from rest_framework import viewsets

from .models import Article
from .serializers import ArticlesSerializers


class ArticlesViewSets(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializers
