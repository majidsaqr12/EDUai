from django.urls import path
from .views import subjects_view

urlpatterns = [
    path('', subjects_view, name='subjects'),
]
