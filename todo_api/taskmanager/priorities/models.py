from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Priority(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='priorities')
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Приоритет"
        verbose_name_plural = "Приоритеты"