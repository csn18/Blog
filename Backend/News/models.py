from django.db import models


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


class NewsCategory(models.Model):
    """
    Model for news category objects
    """
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория новости'
        verbose_name_plural = 'Категории новостей'


class News(models.Model):
    """
    Model for objects of news
    """
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=4096)
    publication_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/news')
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    hash_tags = models.ManyToManyField(HashTags)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
