from django.http import HttpResponseRedirect

from .models import Project, Category, File

from .serializers import ProjectCategoryListSerializer, ProjectsCategorySerializer, ProjectSerializer, FileSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response


class ProjectView(ModelViewSet):
    queryset = Project.objects.filter(status=True)
    serializer_class = ProjectSerializer
    http_method_names = ['get']
    lookup_field = 'slug'


class CategoryView(ModelViewSet):
    queryset = Category.objects.filter(status=True, projects__status=True)
    default_serializer_class = ProjectCategoryListSerializer
    serializer_classes = {
        'list': ProjectCategoryListSerializer,
        'retrieve': ProjectsCategorySerializer
    }
    http_method_names = ['get']
    lookup_field = 'slug'

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class FileView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    http_method_names = ['get']
    serializer_class = FileSerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        try:
            project_slug = kwargs.get('slug', None)
            
            queryset = File.objects.filter(
                project__slug=project_slug,
                project__status=True,
                status=True
            ).first()

            if queryset:
                serializer = FileSerializer(queryset)
                return HttpResponseRedirect(serializer.data.get('files'))
            raise File.DoesNotExist
        except File.DoesNotExist:
            response = dict(detail='Arquivo não encontrado')
            return Response(response, status=status.HTTP_404_NOT_FOUND)
