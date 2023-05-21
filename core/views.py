from django.shortcuts import render
from .models import Page

def home(request):
    page = Page.objects.filter(title="Home").first()
    context = {
        'page': page
    }
    return render(request, 'home.html', context)
