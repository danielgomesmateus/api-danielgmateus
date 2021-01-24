from django.contrib import admin
from .models import AcademicFormation


class AcademicFormationAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'institution',
        'status'
    ]


admin.site.register(AcademicFormation, AcademicFormationAdmin)
