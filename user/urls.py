
from django.contrib import admin
from django.urls import path
from user.views import UserListCreateAPIView,UserDetailAPIView,LoginView

urlpatterns = [
    path('userlist/', UserListCreateAPIView.as_view()),
    path('userdetail/', UserDetailAPIView.as_view()),
    path('userlogin/', LoginView.as_view()),
]
