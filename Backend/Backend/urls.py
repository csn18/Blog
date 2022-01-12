from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from News.router import urlpatterns as news_urls
from Articles.router import urlpatterns as articles_urls

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += news_urls
urlpatterns += articles_urls
