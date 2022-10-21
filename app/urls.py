from django.urls import path, include
from .views import *

urlpatterns = [

    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('posts/', PostList.as_view()),
    path('categories/', CategoryViews.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('slider/', SliderPost.as_view()),
    path('adminpost/', AdminPostList.as_view()),
    path('adminpost/<slug:slug>', EditAdminPostList.as_view()),
    # path('adminpost/<int:title_slug>/', EditAdminPostList.as_view()),
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),
    path('newsletter/', NewsletterEmail.as_view()),
    # path('category/', getCategories),

]