from django.urls import path
from .views import RequirementsListCreateAPIView, RequirementsDetailAPIView

urlpatterns = [
    path('requirement/', RequirementsListCreateAPIView.as_view(), name='requirements-list-create'),
    path('requirement/<int:pk>/', RequirementsDetailAPIView.as_view(), name='requirements-detail'),
]
