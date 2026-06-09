from django.contrib.auth.models import User, AnonymousUser
from django.test import TestCase
from django.urls import reverse
from urllib.parse import urlencode

from .models import Article, UserFavouriteArticle
from .views import ListFavoriteArticles

# Create your tests here.

class FavouritesArticlesAccessTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Porsche', password='Pass@123')
        self.article = Article.objects.create(
            title='Tomobilat',
            author = self.user,
            synopsis = 'Zan van',
            content = 'Smayka sma3 sma3 vaaaaaaaaaaaaaaaaaaan!',
        )
        
    def test_unauthenticated_user_cannot_access_favourite_list(self):
        response = self.client.get(reverse('favoritearticles'))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'articles/favorite_articles.html')
    
    def test_authenticated_user_can_access_favourite_list(self):

        self.client.login(username='Porsche', password='Pass@123')
        response = self.client.get(reverse('favoritearticles'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/favorite_articles.html')

class ArticlesPublicationsAccessTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='Porsche', password='Pass@123')
        self.article = Article.objects.create(
            title='Tomobilat',
            author = self.user,
            synopsis = 'Zan van',
            content = 'Smayka sma3 sma3 vaaaaaaaaaaaaaaaaaaan!',
        )
    def test_unauthenticated_user_cannot_access_publication_page(self):  
        response = self.client.get(reverse('publications'))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'articles/display_publications.html')

    def test_authenticated_user_can_access_publications_page(self):
        self.client.login(username='Porsche', password='Pass@123')
        response = self.client.get(reverse('publications'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/display_publications.html')

class PublishArticlesFunctionalityTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='Porsche', password='Pass@123')
        self.article = Article.objects.create(
            title='Tomobilat',
            author = self.user,
            synopsis = 'Zan van',
            content = 'Smayka sma3 sma3 vaaaaaaaaaaaaaaaaaaan!',
        )

    def test_unauthenticated_users_cannot_access_publish_form(self):
        response = self.client.get(reverse('publish'))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'articles/publish.html')
 
    def test_unauthenticated_users_cannot_submit_publish_form(self):

        data = {
            'title': 'skefkef', 
            'synopsis': 'Nas fih lmakla',
            'content': 'Nas Khobza wla khobza fiha l7am rass jaleft t9alia mhm dakshi lakher',
        }
        response = self.client.post(reverse('publish'), data )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('publish')}" )
        self.assertEqual(Article.objects.count(), 1)

    def test_authenticated_users_can_access_publish_form(self):
        self.client.login(username='Porsche', password='Pass@123')
        response = self.client.get(reverse('publish'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/publish.html')

    def test_authenticated_users_can_submit_publish_form(self):
        self.client.login(username='Porsche', password='Pass@123')
        data = {
            'title': 'skefkef', 
            'synopsis': 'Nas fih lmakla',
            'content': 'Nas Khobza wla khobza fiha l7am rass jaleft t9alia mhm dakshi lakher', 
        }
        response = self.client.post(reverse('publish'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Article.objects.count(), 2)
        
class AddArticleTwiceToFavoriteList(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='Porsche', password='Pass@123')
        self.article = Article.objects.create(
            title='Tomobilat',
            author = self.user,
            synopsis = 'Zan van',
            content = 'Smayka sma3 sma3 vaaaaaaaaaaaaaaaaaaan!',
        )

    def test_unauthenticated_user_cannot_add_article_to_favortie_list(self):
        
        url = reverse('addtofavorite', kwargs={'pk': self.article.pk})
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, 302)
        
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('addtofavorite', kwargs={'pk': self.article.pk})}")
        self.assertEqual(UserFavouriteArticle.objects.count(), 0)
    
    def test_authenticated_user_can_add_article_to_favorite_list(self):
        
        self.client.login(username='Porsche', password='Pass@123')
        url = reverse('addtofavorite', kwargs={'pk': self.article.pk})
        response = self.client.post(url, {})    
        self.assertEqual(response.status_code, 302)

    def test_authenticated_user_cannot_add_same_article_twice_to_favorite_list(self):    

        self.client.login(username='Porsche', password='Pass@123')     
        url = reverse('addtofavorite', kwargs={'pk': self.article.pk})
        self.client.post(url, {})
        self.client.post(url, {})   
        self.assertEqual(UserFavouriteArticle.objects.count(), 1)

class RegistredFormAccessTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Porsche', password='Pass@123')

    def test_authenticated_user_cannot_access_new_registration_form(self):
        self.client.login(username='Porsche', password='Pass@123')
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'registration/signup.html')

    def test_unauthenticated_user_can_access_new_registration_form(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')