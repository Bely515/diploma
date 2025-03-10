from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'priority', 'completed')
    list_filter = ('category', 'priority', 'completed')
    search_fields = ('title', 'description')