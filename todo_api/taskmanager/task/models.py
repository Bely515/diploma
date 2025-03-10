from django.db import models
from django.contrib.auth.models import User

from categories.models import Category
from priorities.models import Priority


# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершено'),
    ]

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks') # related_name позволяет обращаться к задачам пользователя через user.tasks.all().
    title = models.CharField(max_length=100)
    description = models.CharField(blank=True, null=True, max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # автоматически удаляет или изменяет строки из зависимой таблицы при удалении или изменении связанных строк в главной таблице
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)  # Поле для soft delete пользователем

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"