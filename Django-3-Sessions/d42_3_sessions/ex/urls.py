from django.urls import path
from . import views

urlpatterns = [
    path('', views.anonym_users, name='anonym_users'),
    path('registration/', views.Registration.as_view(), name='signup'),


]
