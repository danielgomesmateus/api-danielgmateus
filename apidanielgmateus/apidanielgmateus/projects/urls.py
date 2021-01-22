from rest_framework.routers import SimpleRouter

from .views import ProjectView, CategoryView, FileView
from .models import File

app_name = 'projects'

router = SimpleRouter()
router.register('projects', ProjectView)
router.register('projects-category', CategoryView)
router.register('files', FileView, basename=File)
