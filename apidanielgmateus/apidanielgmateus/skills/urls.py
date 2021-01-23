from rest_framework.routers import SimpleRouter

from .views import SkillView

app_name = 'skills'

router = SimpleRouter()
router.register('skills', SkillView)
