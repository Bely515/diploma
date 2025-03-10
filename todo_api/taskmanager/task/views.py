from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.utils import timezone
from rest_framework import generics
from .serializers import TaskSerializer
from .models import Task
from .forms import TaskForm
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from categories.models import Category
from priorities.models import Priority


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self): # функция для отображения задач текущего пользователя
        user = self.request.user
        queryset = Task.objects.filter(created_by=user, is_deleted=False)

        # Фильтрация по статусу
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)

        # Фильтрация по категории
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)

        # Фильтрация по приоритету
        priority_id = self.request.GET.get('priority')
        if priority_id:
            queryset = queryset.filter(priority_id=priority_id)

        # Фильтрация по ID
        task_id = self.request.GET.get('id')
        if task_id:
            queryset = queryset.filter(id=task_id)

        # Сортировка по статусу, либо времени создания
        sort_by = self.request.GET.get('sort_by')
        if sort_by in ['status', '-status', 'created_at', '-created_at']:
            queryset = queryset.order_by(sort_by)

        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # Получаем все объекты категорий
        context['priorities'] = Priority.objects.all()  # Получаем все объекты приоритетов
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task/task_detail.html'

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/task_update_form.html'
    success_url = reverse_lazy('task_list')

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)

    def form_valid(self, form):
        task = form.save(commit=False)
        task.updated_at = timezone.now()  # Обновляем время редактирования
        task.save()
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, View):
    success_url = reverse_lazy('task_list')
    template_name = 'task/task_confirm_delete.html'

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'], created_by=request.user) # Ищет объект модели Task по указанному первичному ключу (pk) и проверяет создана ли она текущим пользователем.
        return render(request, self.template_name, {'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'], created_by=request.user)
        if request.user.is_superuser:
            task.delete()  # Hard delete для администратора
        else:
            task.is_deleted = True  # Soft delete для пользователя. Устанавливаем флаг True.
            task.save()
        return redirect(self.success_url)



# ---------------- API ----------
class TaskListCreateAPI(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer