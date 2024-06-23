from django.urls import path
from .views import index, posts, recent_posts, post, blog_search, create_post

urlpatterns = [
    path("", index, name="index"),
    path("create-post/", create_post, name="create_post"),
]

htmx_paths =  [
    path("posts/", posts, name='posts'),
    path("recent_posts/", recent_posts, name="recent_posts" ),
    path("post/<int:id>/", post, name="post"),
    path("search-result/", blog_search, name="blog_search"),
    
]

urlpatterns += htmx_paths