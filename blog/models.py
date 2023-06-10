from django.db import models
from core.models import Author
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    category = models.TextField()
    image = models.ImageField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = RichTextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title 
    
    
class Message(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    message = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.email