from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Article, ArticleCategory


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CategoryArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = ['id', 'title']


class ArticlesSerializers(serializers.ModelSerializer):
    hash_tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    author = UserSerializer()
    category = serializers.SlugRelatedField(read_only=True, slug_field='title')

    class Meta:
        model = Article
        fields = ['title', 'text', 'image', 'publication_date', 'author', 'category', 'hash_tags']
