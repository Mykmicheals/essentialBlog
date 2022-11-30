
from turtle import title
import requests
from django.core.management.base import BaseCommand
from django.http import HttpResponse, JsonResponse
from django.db.models import F
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import render
from rest_framework import generics
from .serializers import *

User = get_user_model()


class CategoryViews(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"sucess": "Post has been updated"})

        else:
            return Response({"failed": "failed", "details": serializer.errors})


class UserProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"sucess": "Profile has been updated"})

        else:
            return Response({"failed": "failed", "details": serializer.errors})


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.filter(status=1)
    serializer_class = PostSerializer

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # parser_classes = [MultiPartParser, JSONParser, FormParser]

    # def perform_create(self, serializer):
    #     if serializer.is_valid():
    #         serializer.save(owner=self.request.user)

    #     else:
    #         content = {'failure': ('Please Don"t crash my database.I beg you')}
    #         return Response(content, status=status.HTTP_400_BAD_REQUEST)


class SliderPostView(generics.ListCreateAPIView):
    queryset = SliderPost.objects.all()
    serializer_class = PostSerializer


class SliderPostDetail(generics.RetrieveAPIView):
    queryset = SliderPost.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class AdminPostList(generics.ListAPIView):
    queryset = Post.objects.filter(status=0)
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAdminUser]


class EditAdminPostList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.filter(status=0)
    serializer_class = AdminPostSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'slug'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Post has been updated"})

        else:
            return Response({"message": "failed", "details": serializer.errors})


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    lookup_field = 'slug'


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class NewsletterEmail(generics.CreateAPIView):
    queryset = NewsLetterEmail.objects.all()
    serializer_class = NewsLetterEmailSerilizer


class DescriptionView(generics.ListCreateAPIView):
    queryset = Description.objects.all()
    serializer_class = DescritionSerializer


class ShowNews(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetail(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'slug'




    
