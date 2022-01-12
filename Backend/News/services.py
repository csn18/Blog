from .models import News


def get_all_news():
    """
    Return queryset with news list
    """
    return News.objects.all()
