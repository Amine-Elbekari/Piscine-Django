from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article, UserFavouriteArticle
from django.views.generic import TemplateView
from django.urls import reverse_lazy

# Create your views here.
class ListArticlFields(LoginRequiredMixin, ListView):
    model = Article
    # I choose to give my template file a custom name
    # but you can remove the template_name variable and rename the template file:
    # article_list.html as default template name.
    context_object_name = "articles"
    template_name = 'articles/display_articles.html'

class ListPublications(LoginRequiredMixin, ListView):
    model = Article
    
    context_object_name = "articles"
    template_name = 'articles/display_publications.html'
    
    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)

#This view is used to show the details for the row so it show the detail for one item
class ListDetails(LoginRequiredMixin, DetailView):
    model = Article
    context_object_name = "article"
    template_name = 'articles/details.html'

class ListFavoriteArticles(LoginRequiredMixin, ListView):
    model = UserFavouriteArticle

    context_object_name = "favorite_articles"
    template_name = 'articles/favorite_articles.html'
    def get_queryset(self):
        return UserFavouriteArticle.objects.filter(user=self.request.user)