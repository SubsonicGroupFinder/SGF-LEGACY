from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer

class ListPosts(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


