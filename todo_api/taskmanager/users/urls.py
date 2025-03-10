from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),

    path('profile/', user_profile, name='user-profile'),
    path('change-password/', change_password, name='change-password'),
    path('reset-password/', reset_password, name='reset-password'),
    path('reset-password-confirmation/', reset_password_confirmation, name='reset-password-confirmation'),
    path('soft-delete-user/', soft_delete_user, name='soft-delete-user'),
    path('soft_delete_user/confirmation/', soft_delete_user_confirmation, name='soft-delete-user-confirmation'),
    path('users_list/', users_list, name='users_list'),
    path('users/api/v1/', UserListAPI.as_view(), name='user_list_api'),
]