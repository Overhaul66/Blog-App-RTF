from django.contrib import admin
from .models import Post, Comment, Tag, Category
# Register your models here.

admin.site.register([Post, Comment, Tag, Category])