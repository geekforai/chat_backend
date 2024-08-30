from django.urls import path
from .views import ChatListCreateAPIView, ChatDetailAPIView

urlpatterns = [
    path('chat/', ChatListCreateAPIView.as_view(), name='chat-list-create'),
    path('chat/<int:pk>/', ChatDetailAPIView.as_view(), name='chat-detail'),
]
