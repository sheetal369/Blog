#Django
from django.shortcuts import get_object_or_404
#REST
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import permissions

# Custom
from blog.models import Post
from .serializers import PostSerializer
# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostViewSet(viewsets.ModelViewSet): # Using Model Viewset enables create option as well.
    serializer_class = PostSerializer
    queryset = Post.objects.all()