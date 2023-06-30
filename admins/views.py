# from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Post


class IndexListView(ListView):
    model = Post
    template_name = "admins/index.html"
