from django.urls import path
from . import views
urlpatterns = [
    path('', views.account_view.as_view(), name='account_view'),
    
]
