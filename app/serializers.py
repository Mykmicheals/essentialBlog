from dataclasses import field
from pyexpat import model
from unicodedata import category
from django.utils.text import slugify
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import *

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'posts',
                  'comments', 'is_staff', 'last_name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['name', 'id']


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.first_name')
    comments = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True, )
    created = serializers.DateTimeField(format="%d-%m-%Y", read_only=True,)
    # category = serializers.CharField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'description',
                  'owner', 'comments', 'image', 'created', 'slug']
        # fields = '__all__'


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
