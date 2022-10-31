from dataclasses import field, fields
from pyexpat import model
from unicodedata import category
from django.utils.text import slugify
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import *

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')

    class Meta:
        model = Profile
        fields = '__all__'


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'description']


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=True)
    posts = UserPostSerializer(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'posts',
                  'comments', 'is_staff', 'last_name', 'profile']
        depth = 1

        def create(self, validated_data):
            user = User.objects.create(
                # url=validated_data['url'],
                email=validated_data['email'],
                # etc ...
            )
            profile_data = validated_data.pop('profile')
            profile = Profile.objects.create(
                user=user,
                first_name=profile_data['first_name'],
            )

            return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['name', 'id']


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.first_name')
    comments = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True, )
    created = serializers.DateTimeField(format="%d-%m-%Y", read_only=True,)
    owner_id = serializers.ReadOnlyField(source='owner.id')
    # category = serializers.CharField()

    class Meta:
        model = Post
        # fields = ['id', 'title', 'description',
        #           'owner_id', 'comments', 'image', 'created', 'slug']
        fields = '__all__'


class SliderPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = SliderPost
        fields = '__all__'


class AdminPostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.first_name')
    created = serializers.DateTimeField(format="%d-%m-%Y", read_only=True,)
    slug = serializers.SerializerMethodField()

    def get_slug(self, instance):
        return slugify(instance.title)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description',
                  'owner', 'status', 'created', 'image', 'slug']


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.first_name')
    owner_id = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'post', 'owner_id']


class NewsLetterEmailSerilizer(serializers.ModelSerializer):

    class Meta:
        model = NewsLetterEmail
        fields = '__all__'


class DescritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = '__all__'
