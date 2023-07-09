#Django
from django.shortcuts import get_object_or_404
#REST
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
# Custom
from blog.models import Post
from .serializers import PostSerializer

# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    #Changes