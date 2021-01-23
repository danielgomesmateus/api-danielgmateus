from .models import Skill
from .serializers import SkillSerializer

from rest_framework import viewsets, mixins


class SkillView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Skill.objects.filter(status=True)
    serializer_class = SkillSerializer
    http_method_names = ['get']
