from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category
from .forms import PostForm
# Create your views here.
def index(request):
    return render(request, "posts/index.html")

def post(request, id):
    post = Post.objects.get(pk=id)
    return render(request, "posts/post.html", {'post':post})

def posts(request):
    categories = [c for c in Category.objects.all()] #fetch all catergories from db
    post_categories = dict()
    for category in categories:
        post_categories[category.name] = Post.objects.filter(category=category)
    
    return render(request, "posts/partials/posts.html", {"posts_categories":post_categories})

def recent_posts(request):
    posts = Post.objects.order_by('-date_created', '-last_update')
    return render(request, "posts/partials/recent_posts.html", {"posts":posts} )

def blog_search(request):
    if request.method == "POST":
        search_key  = request.POST["search"]
        posts = Post.objects.filter(title__icontains=search_key)
    return render(request, "posts/partials/search_results.html", {"posts":posts})

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return 
        else:
            return render(request, "posts/post_create.html", {"form" : form})
    form = PostForm()
    return render(request, "posts/post_create.html", {"form" : form})