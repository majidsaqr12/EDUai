from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap

urlpatterns = [
    path('', views.home, name='home'),
    path('success/', views.success_view, name='success'),
]
