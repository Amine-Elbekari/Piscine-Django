from django.urls import path
from . import views

urlpatterns = [
    path('', views.dynamic_table, name='dynamic_table'),
]
