from rest_framework.routers import SimpleRouter

from .views import ExperienceView

app_name = 'experiences'

router = SimpleRouter()
router.register('experiences', ExperienceView)
