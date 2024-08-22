from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create_user),
    path('name', views.get_name),
    path('signup', views.signup),
]
