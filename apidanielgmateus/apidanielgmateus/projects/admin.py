from django.contrib import admin
from .models import Project, Category


class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'name', 
        'category',
        'slug',
        'status'
    ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'status'
    ]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
