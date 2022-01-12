from django.urls import path, include
from rest_framework import routers

from .api import NewsViewSet

router = routers.DefaultRouter()
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]
