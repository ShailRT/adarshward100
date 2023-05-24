from django.shortcuts import render
from .models import Page, News

def home(request):
    page = Page.objects.filter(title="Home").first()
    news = News.objects.all()[:4]
    context = {
        'page': page,
        'news': news
    }
    return render(request, 'home.html', context)
