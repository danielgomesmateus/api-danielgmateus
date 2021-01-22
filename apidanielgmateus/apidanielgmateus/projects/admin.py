from django.contrib import admin
from .models import Project, Category, File


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


class FileAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'version',
        'status'
    ]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(File, FileAdmin)
