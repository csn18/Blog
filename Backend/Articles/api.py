from rest_framework import viewsets

from .models import Article
from .serializers import ArticlesSerializers
from .services import get_all_articles


class ArticlesViewSets(viewsets.ModelViewSet):
    queryset = get_all_articles()
    serializer_class = ArticlesSerializers
