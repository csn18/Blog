from django.contrib import admin
from .models import *

admin.site.register(HashTags)
admin.site.register(ArticleCategory)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'author', 'category']
    list_editable = ['author', 'category']
