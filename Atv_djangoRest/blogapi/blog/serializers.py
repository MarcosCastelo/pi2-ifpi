from rest_framework import serializers
from .models import *




def load_json():
    json_file = open('db.json', 'r')
    dict_json = json.load(json_file)


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
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        address_data = validated_data.pop('address')
        address = instance.address
        address.street = address_data.get('street', address.street)
        address.suite = address_data.get('suite', address.suite)
        address.city = address_data.get('city', address.city)
        address.zipcode = address_data.get('zipcode', address.zipcode)

        address.save()
        instance.save()
        return instance


class ProfilePostSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.SlugRelatedField(
        many=True,
        queryset = Post.objects.all(),
        slug_field='title',
    )
    class Meta:
        model = Profile
        fields = ('name', 'posts')