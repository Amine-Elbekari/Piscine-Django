from django.urls import path
from .views import ListArticlFields, ListPublications, ListDetails, ListFavoriteArticles

urlpatterns = [
    path("articles/", ListArticlFields.as_view(), name='home'),
    path("details/<int:pk>/", ListDetails.as_view(), name='details'),
    path("publications/", ListPublications.as_view(), name='publications'),
    path("favoritearticles/", ListFavoriteArticles.as_view(), name='favoritearticles'),


]
