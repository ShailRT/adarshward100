from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model

User = get_user_model()

title_choices =(
    ('Media Prabhari', 'media prabhari'),
    ('Counselor', 'counselor'),
    ('Citizen', 'citizen'),
    ('Mayor', 'mayor')
)

class Page(models.Model):
    title = models.CharField(max_length=120)
    urls = models.CharField(max_length=200)
    content = RichTextField()

    def __str__(self):
        return self.title

class Navbar(models.Model):
    title = models.CharField(max_length=120)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="page")
    sub_menu = models.ManyToManyField(Page, related_name="sub_menu", null=True, blank=True)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    title = models.CharField(max_length=120)
    on_gallery = models.BooleanField(default=False)
    image = models.ImageField(upload_to='gallery/')

    class Meta:
        ordering = ['on_gallery']

    def __str__(self):
        return self.title
    
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile/', null=True, blank=True)
    phone = models.CharField(max_length=12)
    title = models.CharField(max_length=120, choices=title_choices, default="citizen")
    address = models.CharField(max_length=200, blank=True, null=True)
    house_number = models.CharField(max_length=10)
    bio = models.TextField(blank=True, null=True)
    whatsapp_groups = models.TextField(blank=True, null=True)
    instagram = models.CharField(max_length=120, blank=True, null=True)
    twitter = models.CharField(max_length=120, blank=True, null=True)
    facebook = models.CharField(max_length=120, blank=True, null=True)


    def __str__(self):
        return self.user.email 
    
class Anouncement(models.Model):
    title = models.TextField()
    file = models.FileField(upload_to="anouncement/", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 
    
class Author(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=120)
    
    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    image = models.ImageField(upload_to='news/')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = RichTextField()
    gallery = models.ManyToManyField(Gallery, related_name='news_gallery', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title
    
    

    
