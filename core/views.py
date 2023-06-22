from django.shortcuts import render, redirect
from .models import Page, News, Gallery, News, Profile, Anouncement
from django.contrib.auth.models import User, auth
from django.contrib import messages

def home(request):
    page = Page.objects.filter(title="Home").first()
    news = News.objects.all()[:9]
    anouncements = Anouncement.objects.all()[:9]
    home_slider = Gallery.objects.filter(on_home_slider=True)
    context = {
        'page': page,
        'news': news,
        'anouncements': anouncements,
        'home_slider': home_slider,
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
        address = request.POST['address']
        redirect_to = request.POST['redirect_to']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        username = aadhaar
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User Exists')
                return redirect(redirect_to)
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                user.save()
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
            
                user = User.objects.filter(username=username).first()
                profile = Profile.objects.create(user=user, phone=phone, house_number=house_no, address=address)
                profile.save()
                return redirect(redirect_to)
    else:
        return redirect('/')
    
def signin(request):
    if request.method == "POST":
        username = request.POST['aadhaar']
        password = request.POST['password']
        redirect_to = request.POST['redirect_to']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect(redirect_to)
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect(redirect_to)    
        
def logout(request):
    auth.logout(request)
    redirect_to = request.GET.get('redirect_to')
    return redirect(redirect_to)
        
def profile(request, pk):
    user = User.objects.filter(username=pk).first()
    profile = Profile.objects.filter(user=user).first()

    context = {
        'profile': profile,
    }
    return render(request, 'profile/profile.html', context)
