from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskssAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'creator', 'created', 'updated', 'status','assigned_to']
    list_filter = ['status', 'created', 'updated', 'creator']
    search_fields = ['title', 'description', 'creator', 'assigned_to']
    prepopulated_fields = {'slug': ('title',)}
