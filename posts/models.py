from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250, unique=True, null=False)
    content =CKEditor5Field('Text', config_name='extends')
    date_created = models.DateTimeField(auto_now=True)
    last_update = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', related_name="posts", blank=True)
    category = models.ForeignKey("Category", related_name="posts", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(default='', blank=False, null=False)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:10]

class Tag(models.Model):
    tag_name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.tag_name

class Category(models.Model):
    name = models.CharField(max_length=180)

    def __str__(self):
        return self.name
    
