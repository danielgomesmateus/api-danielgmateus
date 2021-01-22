from rest_framework.routers import SimpleRouter

from .views import PostView, CategoryView

app_name = 'posts'

router = SimpleRouter()
router.register('posts', PostView)
router.register('posts-category', CategoryView)
