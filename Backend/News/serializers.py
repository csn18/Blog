from django.contrib.auth.models import User
from rest_framework import serializers

from .models import News, NewsCategory


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CategoryNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = ['id', 'title']


class NewsSerializers(serializers.ModelSerializer):
    hash_tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    author = UserSerializer()
    category = serializers.SlugRelatedField(read_only=True, slug_field='title')

    class Meta:
        model = News
        fields = ['title', 'text', 'image', 'publication_date', 'category', 'hash_tags']