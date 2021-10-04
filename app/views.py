
from urllib.parse import parse_qs
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


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.filter(status=1)
    serializer_class = PostSerializer
    print(serializer_class)
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # parser_classes = [MultiPartParser, JSONParser, FormParser]

    def perform_create(self, serializer):
        if serializer.is_valid():
            print(serializer)
            serializer.save(owner=self.request.user)

        else:
            content = {'failure': ('Please Don"t crash my database.I beg you')}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


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


# class EditAdminPostList(generics.RetrieveUpdateDestroyAPIView):
class EditAdminPostList(generics.RetrieveAPIView):
    queryset = Post.objects.filter(status=0)
    serializer_class = AdminPostSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'slug'


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
