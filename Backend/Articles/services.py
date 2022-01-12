from .models import Article


def get_all_articles():
    """
    Returned all articles
    """
    return Article.objects.all()
