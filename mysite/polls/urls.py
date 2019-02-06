from django.urls import path, re_path

from . import views

urlpatterns = [
    path(r'', views.read, name='read'),
    path(r'login/', views.login),
    path(r'generation/', views.generation)
]