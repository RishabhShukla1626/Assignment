from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.generator, name="generator"),
    path("/generated-password", views.password, name="password"),
]
