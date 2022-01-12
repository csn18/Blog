from rest_framework import viewsets

from .serializers import NewsSerializers
from .services import get_all_news


class NewsViewSet(viewsets.ModelViewSet):
    """
    View for get list news
    """
    queryset = get_all_news()
    serializer_class = NewsSerializers
