from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.reverse import reverse
from .models import *
from .serializers import *

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    
    def get(self, request, *args, **kwargs):
        return Response({
            'profiles' : reverse(ProfileList.name, request=request),
            'posts' : reverse(PostList.name, request=request),
            'comments' : reverse(CommentList.name, request=request),
            'profile-posts' : reverse(ProfilePostList.name, request=request),
            'post-comments' : reverse(PostCommentList.name, request=request),
        })

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-list'

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-detail'

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-list'

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-detail'

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-detail'

class ProfilePostList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerializer
    name = 'profile-post-list'

class ProfilePostDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerializer
    name = 'profile-post-detail'

class PostCommentList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCommentSerializer
    name = 'post-comment-list'

class PostCommentDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCommentSerializer
    name = 'post-comment-detail'