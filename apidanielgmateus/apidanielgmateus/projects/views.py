from .models import Project, Category

from .serializers import ProjectCategoryListSerializer, ProjectsCategorySerializer, ProjectSerializer

from rest_framework.viewsets import ModelViewSet


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
