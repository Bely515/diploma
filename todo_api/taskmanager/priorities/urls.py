from django.urls import path
from .views import *

urlpatterns = [
    path('', PriorityListView.as_view(), name='priority_list'),
    path('add/', PriorityCreateView.as_view(), name='priority_add'),
    path('<int:pk>/', PriorityDetailView.as_view(), name='priority_detail'),
    path('edit/<int:pk>/', PriorityUpdateView.as_view(), name='priority_edit'),
    path('delete/<int:pk>/', PriorityDeleteView.as_view(), name='priority_delete'),
    path('api/v1/', PriorityListAPI.as_view(), name='priority_list_api'),
]
