from django.urls import path
from .views import ListArticlFields, ListPublications, ListDetails, ListFavoriteArticles, SignUpView, PublishView
urlpatterns = [
    path("articles/", ListArticlFields.as_view(), name='home'),
    path("details/<int:pk>/", ListDetails.as_view(), name='details'),
    path("publications/", ListPublications.as_view(), name='publications'),
    path("favoritearticles/", ListFavoriteArticles.as_view(), name='favoritearticles'),
    path("register/", SignUpView.as_view(), name='register'),
    path("publish/", PublishView.as_view(), name='publish')
]
