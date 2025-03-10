from django.urls import path
from .views import *

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('add/', CategoryCreateView.as_view(), name='category_add'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('edit/<int:pk>/', CategoryUpdateView.as_view(), name='category_edit'),
    path('delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('api/v1/', CategoryListAPI.as_view(), name='category_list_api'),
]
