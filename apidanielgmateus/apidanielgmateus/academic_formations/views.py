from .models import AcademicFormation
from .serializers import AcademicFormationSerializer

from rest_framework import viewsets, mixins


class AcademicFormationView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = AcademicFormation.objects.filter(status=True)
    serializer_class = AcademicFormationSerializer
    http_method_names = ['get']
