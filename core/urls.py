from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('gallery/', views.gallery, name="gallery"),
    path('news/<str:pk>/', views.news_detail, name="news_detail"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name="logout"),
    path('signin/', views.signin, name="signin"),
    path('profile/<str:pk>/', views.profile, name="profile"),
]
