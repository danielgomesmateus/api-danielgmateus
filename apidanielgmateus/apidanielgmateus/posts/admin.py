from django.contrib import admin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
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


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
