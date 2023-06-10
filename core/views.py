from django.shortcuts import render, redirect
from .models import Page, News, Gallery, News, Profile
from django.contrib.auth.models import User, auth
from django.contrib import messages

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
    similar_news = News.objects.all()[:3]
    context = {
        'news': news,
        'similar_news': similar_news,
    }
    return render(request, 'news/news.html', context)

def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        aadhaar = request.POST['aadhaar']
        email = request.POST['email']
        house_no = request.POST['house_no']
        redirect_to = request.POST['redirect_to']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        username = aadhaar
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email)
                user.save()
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
            
                user = User.objects.filter(username=username).first()
                profile = Profile.objects.create(user=user, phone=phone, house_number=house_no)
                profile.save()
                return redirect('/')
        
