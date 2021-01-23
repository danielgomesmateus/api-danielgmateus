from rest_framework import serializers
from .models import Experience


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = (
            'title',
            'company',
            'description',
            'image',
            'started_at',
            'ended_at'
        )
