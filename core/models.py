from django.db import models
from ckeditor.fields import RichTextField

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

    