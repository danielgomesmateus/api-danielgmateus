from rest_framework.routers import SimpleRouter

from .views import AcademicFormationView

app_name = 'academic_formations'

router = SimpleRouter()
router.register('academic-formations', AcademicFormationView)
