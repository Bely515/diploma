from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Priority
from .forms import PriorityForm
from django.utils import timezone
from rest_framework import generics
from .serializers import PrioritySerializer


# Create your views here.
class PriorityListView(LoginRequiredMixin, ListView):
    model = Priority
    template_name = 'priorities/priority_list.html'
    context_object_name = 'priorities'

    def get_queryset(self):
        return Priority.objects.filter(created_by=self.request.user)


class PriorityCreateView(LoginRequiredMixin, CreateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priorities/priority_form.html'
    success_url = reverse_lazy('priority_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class PriorityUpdateView(LoginRequiredMixin, UpdateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priorities/priority_update_form.html'
    success_url = reverse_lazy('priority_list')

    def get_queryset(self):
        return Priority.objects.filter(created_by=self.request.user)

    def form_valid(self, form):
        priority = form.save(commit=False)
        priority.updated_at = timezone.now()  # Обновляем время редактирования
        priority.save()
        return super().form_valid(form)


class PriorityDeleteView(LoginRequiredMixin, DeleteView):
    model = Priority
    template_name = 'priorities/priority_confirm_delete.html'
    success_url = reverse_lazy('priority_list')

    def get_queryset(self):
        return Priority.objects.filter(created_by=self.request.user)


class PriorityDetailView(LoginRequiredMixin, DetailView):
    model = Priority
    template_name = 'priorities/priority_detail.html'

    def get_queryset(self):
        return Priority.objects.filter(created_by=self.request.user)


# ---------------- API ----------
class PriorityListAPI(generics.ListCreateAPIView):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer