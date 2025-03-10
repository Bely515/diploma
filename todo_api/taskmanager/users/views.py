from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from rest_framework import generics
from .serializers import UserProfileSerializer


User = get_user_model() # для получения текущей модели пользователя


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('task_list')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def user_profile(request):
    user = request.user
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()
        return redirect('user-profile')
    return render(request, 'users/user_profile.html', {'user': user})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # обновляем сессию для пользователя
            messages.success(request, 'Ваш пароль был успешно обновлен!')
            return redirect('user-profile')
        else:
            messages.error(request, 'Пароли не совпадают.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        'form': form
    })


@login_required
def reset_password(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)  # Обновляем сессию для пользователя
            return redirect('reset-password-confirmation')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'users/reset_password.html', {'form': form})


@login_required
def reset_password_confirmation(request):
    return render(request, 'users/reset_password_confirmation.html')


@login_required
def soft_delete_user(request):
    if request.method == 'POST':
        user = request.user
        user.is_active = False  # Делаем пользователя неактивным
        user.save()
        logout(request)  # Выход из учетной записи
        return redirect('soft-delete-user-confirmation')
    return render(request, 'users/soft_delete_user.html')


@login_required
def soft_delete_user_confirmation(request):
    return render(request, 'users/soft_delete_user_confirmation.html')


@login_required
def users_list(request):
    sort_by = request.GET.get('sort_by', 'id') # По умолчанию сортировка по 'id'
    if sort_by not in ['id', 'username']:
        sort_by = 'id'  # Обеспечить безопасную сортировку

    users = User.objects.filter(is_active=True).order_by(sort_by)
    return render(request, 'users/users_list.html', {'users': users})


# ---------------- API ----------
class UserListAPI(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
