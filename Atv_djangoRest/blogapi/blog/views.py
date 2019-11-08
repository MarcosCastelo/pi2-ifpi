from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.reverse import reverse
from .models import *
from .serializers import *
import json

def load_json(request):
    json_file = open('db.json', 'r')
    dict_json = json.load(json_file)

    for user in dict_json['users']:
        address = Address.objects.create(
            street = user['address']['street'],
            suite = user['address']['suite'],
            city = user['address']['city'],
            zipcode = user['address']['zipcode'],
        )
        profile = Profile.objects.create(
            id = user['id'],
            name = user['name'],
            email = user['email'],
            address = address
        )
    for post in dict_json['posts']:
        profile = Profile.objects.get(pk=post['userId'])
        Post.objects.create(
            id = post['id'],
            title = post['title'],
            body = post['body'],
            profile = profile
        )
    for comment in dict_json['comments']:
        post = Post.objects.get(pk=comment['postId'])
        Comment.objects.create(
            id = comment['id'],
            name=comment['name'],
            email=comment['email'],
            body=comment['body'],
            post=post
        )

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    
    def get(self, request, *args, **kwargs):
        return Response({
            'profiles' : reverse(ProfileList.name, request=request),
            'posts' : reverse(PostList.name, request=request),
            'comments' : reverse(CommentList.name, request=request),
            'profile-posts' : reverse(ProfilePostList.name, request=request),
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