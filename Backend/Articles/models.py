from django.contrib.auth.models import User
from django.db import models


class ArticleCategory(models.Model):
    """
    Model for articles category objects
    """
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория статей'
        verbose_name_plural = 'Категории статей'


class HashTags(models.Model):
    """
    Model for article hashtag objects
    """
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Хэштег'
        verbose_name_plural = 'Хэштеги'


class Article(models.Model):
    """
    Model for objects of articles
    """
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=4096)
    publication_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/articles')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE)
    hash_tags = models.ManyToManyField(HashTags)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
