from django.urls import path
from .views import ListArticlFields

urlpatterns = [
    path("articles/", ListArticlFields.as_view(), name='home'),

]
