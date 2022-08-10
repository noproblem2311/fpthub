from django.shortcuts import render
from .models import Topic,Post
from .serializers import PostSerializer, TopicSerializer
from rest_framework import viewsets, permissions



class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(active=True)
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

