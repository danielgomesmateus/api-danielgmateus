from .models import Skill
from .serializers import SkillSerializer

from rest_framework.viewsets import ModelViewSet


class SkillView(ModelViewSet):
    queryset = Skill.objects.filter(status=True)
    serializer_class = SkillSerializer
    http_method_names = ['get']
