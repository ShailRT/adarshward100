from django.shortcuts import render
from .models import Page, News, Gallery, News

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

def gallery(request):
    gallery = Gallery.objects.filter(on_gallery=True)
    page = Page.objects.filter(title="Gallery").first()
    context = {
        'gallery': gallery,
        'page': page
    }
    return render(request, 'gallery.html', context)

def news_detail(request, pk):
    news = News.objects.filter(slug=pk).first()
    context = {
        'news': news
    }
    return render(request, 'news/news.html', context)