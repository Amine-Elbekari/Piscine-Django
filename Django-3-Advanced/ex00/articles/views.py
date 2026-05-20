from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import ListView
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
    template_name = 'ex00/display_articles.html'
