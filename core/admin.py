from django.contrib import admin
from .models import Navbar, Page, News, Author


admin.site.register(Page)
admin.site.register(News)
admin.site.register(Navbar)
admin.site.register(Author)
