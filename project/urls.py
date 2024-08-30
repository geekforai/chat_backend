from django.urls import path
from .views import ProjectListCreateAPIView, ProjectDetailAPIView

urlpatterns = [
    path('project/', ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('project/<int:pk>/', ProjectDetailAPIView.as_view(), name='project-detail'),
]

