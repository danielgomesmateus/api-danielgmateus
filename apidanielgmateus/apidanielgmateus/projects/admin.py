from django.contrib import admin
from .models import Project, Category, File


class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'name', 
        'categorie', 
        'slug',
        'status'
    ]


class CategorieAdmin(admin.ModelAdmin):
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
admin.site.register(Category, CategorieAdmin)
admin.site.register(File, FileAdmin)
