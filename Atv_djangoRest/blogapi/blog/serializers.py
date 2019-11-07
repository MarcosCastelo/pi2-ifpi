from rest_framework import serializers
from .models import *

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('street', 'suite', 'city', 'zipcode')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body', 'post')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'body', 'profile')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = Profile
        fields = ('name', 'email', 'address')

class ProfilePostSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.SlugRelatedField(
        many=True,
        queryset = Post.objects.all(),
        slug_field='title',
    )
    class Meta:
        model = Profile
        fields = ('name', 'posts')

class PostCommentSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)
    class Meta:
        model = Post
        fields = ('title', 'comments')