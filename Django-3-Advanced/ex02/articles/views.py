from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import Article, UserFavouriteArticle
from .forms import PublicationForm

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

class SignUpView(CreateView):
    
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')
    
    # Use this to redirect user directly to home page after registration rather then login
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    # Automatically logs in the user the moment they register successfully
    # def form_valid(self, form):
    #     user = form.save()
    #     login(self.request, user)
    #     return redirect('home')

class PublishView(LoginRequiredMixin,CreateView):
    
    form_class = PublicationForm 
    
    template_name = 'articles/publish.html'
    context_object_name = 'form'
    success_url = reverse_lazy('publish')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)