
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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser, JSONParser, FormParser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SliderPost(generics.ListCreateAPIView):
    queryset = SliderPost.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAdminUser]


class AdminPostList(generics.ListAPIView):
    queryset = Post.objects.filter(status=0)
    serializer_class = AdminPostSerializer
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
# Create your views here.
    # lookup_field = 'pk'


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

    # def post(self, request):
    #     serializer = NewsLetterEmail(email=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data={'sucess': 'email succesfully added '}, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(data={'error': 'invalid email address '}, status=status.HTTP_400_BAD_REQUEST)


# def getCategories(request):
#     cat = Post.objects.filter(category__contains='sports')
#     print(cat)
#     serializer = PostSerializer(cat, many=True)
#     return JsonResponse(serializer.data, safe=False)
