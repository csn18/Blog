from django.urls import path, include
from rest_framework import routers

from .api import ArticlesViewSets

router = routers.DefaultRouter()
router.register(r'articles', ArticlesViewSets)

urlpatterns = [
    path('', include(router.urls))
]
