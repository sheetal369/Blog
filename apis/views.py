from django.shortcuts import render
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer

# Create your views here.
class PostAPIView(generics.ListAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer