from .models import Experience
from .serializers import ExperienceSerializer

from rest_framework import viewsets, mixins


class ExperienceView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Experience.objects.filter(status=True)
    serializer_class = ExperienceSerializer
    http_method_names = ['get']
