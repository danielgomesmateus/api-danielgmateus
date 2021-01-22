from rest_framework.serializers import ModelSerializer

from .models import Project, Category, File


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = (
            'name', 
            'description_short', 
            'content', 
            'cover_image',
            'slug'
        )


class ProjectCategoryListSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'name',
            'slug'
        )


class ProjectsCategorySerializer(ModelSerializer):

    projects = ProjectSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            'name',
            'slug',
            'projects'
        )


class FileSerializer(ModelSerializer):

    class Meta:
        model = File
        lookup_field = 'slug'
        fields = (
            'files',
        )
