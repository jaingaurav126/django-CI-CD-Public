from django.urls import path
from .views import deploy_view

urlpatterns = [
    path('', deploy_view, name='deploy'),
]
