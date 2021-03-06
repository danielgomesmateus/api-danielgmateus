from rest_framework import serializers
from .models import AcademicFormation


class AcademicFormationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicFormation
        fields = (
            'name',
            'institution',
            'started_at',
            'ended_at',
            'image'
        )
