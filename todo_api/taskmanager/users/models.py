from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

 #Create your models here.
class CustomUser(AbstractUser): # немного изменил, чтобы избежать конфликтов обратной связи с другими моделями.
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True) # Указываем уникальное имя для обратного доступа
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)
