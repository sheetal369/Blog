from django.shortcuts import render
from django.http import request
from django.contrib.auth.decorators import login_required
from blog.models import Post



def index(request):
    posts = Post.published.all()
    return render(request, "core/index.html", {"posts": posts})  # normal user

@login_required
def my_blogs(request):
    posts = request.user.my_blogs.all()
    return render(request, "core/my_blogs.html", {"posts": posts})
