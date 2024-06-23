from django import forms
from .models import Post
from django_ckeditor_5.widgets import CKEditor5Widget

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ("title", "tags", "category", "content")
        widgets = {
            "content":CKEditor5Widget(
                attrs={"class":"django_ckeditor_5"}, config_name="extends"
            )
        }
