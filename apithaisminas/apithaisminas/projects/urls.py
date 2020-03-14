from django.urls import path
from .views import ProjectView

app_name = 'project'

urlpatterns = [
    path('', ProjectView.as_view({'get': 'list'}), name='api-project-list'),
    path('<slug:slug>/', ProjectView.as_view({'get': 'retrieve'}), name='api-project-get')
]