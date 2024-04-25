from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.TextField(unique=True, null=False)
    content = RichTextField()
    date_created = models.DateTimeField(auto_now=True)
    last_update = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', related_name="posts", null=True, blank=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(default='', blank=False, null=False)
    date_created = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    tag_name = models.CharField(max_length=100, blank=False, null=False)
