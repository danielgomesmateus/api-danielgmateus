from django.http import HttpResponse, FileResponse

from .models import Project, Categorie, File
from .serializers import CategorieSerializer, CategorieProjectsSerializer, ProjectSerializer, FileSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.renderers import BaseRenderer
from rest_framework.decorators import action


class ProjectFilesRenderer(BaseRenderer):
    media_type = ''
    format = ''

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data


class ProjectView(ModelViewSet):
    queryset = Project.objects.filter(status=True)
    serializer_class = ProjectSerializer
    http_method_names = ['get']
    lookup_field = 'slug'


class CategorieView(ModelViewSet):
    queryset = Categorie.objects.filter(status=True, projects__status=True)
    default_serializer_class = CategorieSerializer
    serializer_classes = {
        'list': CategorieSerializer,
        'retrieve': CategorieProjectsSerializer
    }
    http_method_names = ['get']
    lookup_field = 'slug'

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class FileView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    http_method_names = ['get']

    @action(detail=True, renderer_classes=(ProjectFilesRenderer,))
    def project_files(self, serializer):
        try:
            response = HttpResponse(serializer.get('files'), content_type='application/*')
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(serializer.get('files'))
            
            return response
        except File.DoesNotExist:
            HttpResponse('Arquivo não encontrado')

    def retrieve(self, request, *args, **kwargs):
        try:
            queryset = File.objects.get(pk=kwargs.get('pk'))
            serializer = FileSerializer(queryset)

            response = self.project_files(serializer.data)

            return response
        except File.DoesNotExist:
            HttpResponse('Arquivo não encontrado')
