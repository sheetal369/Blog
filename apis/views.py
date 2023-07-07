from django.shortcuts import render
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.response import Response

#Rest_framework 'View_set' tutorial

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostViewSet(viewsets.ViewSet):
    def list(self, request):
        query_set = Post.objects.all()
        serializer = PostSerializer(query_set, many = True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        query_set = Post.objects.all()
        user = get_object_or_404(query_set, pk=pk)
        serializer = PostSerializer(user)
        return Response(serializer.data)