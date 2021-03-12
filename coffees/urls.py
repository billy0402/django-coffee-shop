from django.urls import path

from . import views

urlpatterns = [
    # ex: /coffees/
    path('', views.index),
]
