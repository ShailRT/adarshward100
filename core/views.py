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

def about(request):
    page = Page.objects.filter(title="About").first()
    context = {
        'page': page,
    }
    return render(request, 'about.html', context)

def contact(request):
    page = Page.objects.filter(title="Contact").first()
    context = {
        'page': page,
    }
    return render(request, 'contact.html', context)
