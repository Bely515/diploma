from django.urls import path
from .views import *


urlpatterns = [
    path('list/', TaskListView.as_view(), name='task_list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('add/', TaskCreateView.as_view(), name='task_add'),
    path('edit/<int:pk>/', TaskUpdateView.as_view(), name='task_edit'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
    path('api/v1/', TaskListCreateAPI.as_view(), name='task_list_create_api'),
    path('api/v1/<int:pk>/', TaskRetrieveUpdateDestroyAPI.as_view(), name='task_detail_api'),
]
