from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['status']
    list_filter = ['created', 'status']
    list_display = ['title', 'author',  'status']
    search_fields = ['author', 'title']
