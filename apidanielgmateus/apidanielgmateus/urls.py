"""apidanielgmateus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .contacts.urls import router as contacts_router
from .pages.urls import router as pages_router
from .projects.urls import router as projects_router
from .slides.urls import router as slides_router
from .posts.urls import router as posts_router

router = DefaultRouter()

router.registry.extend(contacts_router.registry)
router.registry.extend(pages_router.registry)
router.registry.extend(projects_router.registry)
router.registry.extend(slides_router.registry)
router.registry.extend(posts_router.registry)

schema_view = get_schema_view(
    openapi.Info(
        title="danielgmateus API",
        default_version='v1',
        description="API description",
        contact=openapi.Contact(email="contato@danielgmateus.com.br")
    ),
    public=False,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
    path('v1/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger')
]
