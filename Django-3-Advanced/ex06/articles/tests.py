from django.contrib.auth.models import User, AnonymousUser
from django.test import TestCase
from django.urls import reverse
from urllib.parse import urlencode

from .models import Article, UserFavouriteArticle
from .views import ListFavoriteArticles

# Create your tests here.

class test_favourites_articles_accesebility(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Porsche', password='Pass@123')
        self.article = Article.objects.create(
            title='Tomobilat',
            author = self.user,
            synopsis = 'Zan van',
            content = 'Smayka sma3 sma3 vaaaaaaaaaaaaaaaaaaan!',
        )
        
    def test_unauthenticated_user(self):
        response = self.client.get(reverse('favoritearticles'))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'articles/favorite_articles.html')
    def test_authenticated_user(self):

        self.client.login(username='Porsche', password='Pass@123')
        response = self.client.get(reverse('favoritearticles'))
        self.assertEqual(response.status, 200)
        self.assertTemplateUsed(response, 'articles/favorite_articles.html')

class test_add_article_twice_to_favorite_list(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='Porsche', password='Pass@123')
        self.article = Article.objects.create(
            title='Tomobilat',
            author = self.user,
            synopsis = 'Zan van',
            content = 'Smayka sma3 sma3 vaaaaaaaaaaaaaaaaaaan!',
        )

    def test_add_to_favorite_list_for_authenticated_users(self):
        
        self.client.login(username='Porsche', password='Pass@123')     
        response = self.client.post(reverse('addtofavorite', kwargs={'pk': self.article.pk}), {})    
        self.assertEqual(response.status_code, 302)
        self.assertTrue(UserFavouriteArticle.objects.filter(article=self.article).exists())

    def test_add_to_favorite_list_for_unauthenticated_users(self):
        pass