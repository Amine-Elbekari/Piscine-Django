from django.contrib.auth.models import User
from django.test import TestCase
from .models import Article, UserFavouriteArticle


# Create your tests here.

class favourites_articles_accesebility_by_registred_users(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='AbdElMajid', password="Pass@123")
        self.user2 = User.objects.create_user(username='Zoubida', password='Pass@123')
        self.user3 = User.objects.create_user(username='Anass', password='Pass@123')
        
        self.article1 = Article.objects.create(
            title='Taalime',
            author = self.user1,
            created = '2026-05-15T10:30:00Z',
            synopsis = 'Tikchbila tiwliwla',
            content = 'Taalim chi haja mzyana khassna n9raw o n7tarmo l2ostad',
        )
        self.article2 = Article.objects.create(
            title='Legend of Cooking',
            author = self.user2,
            created = '2026-05-12T10:30:00Z',
            synopsis = 'Cooking is something doing with love',
            content = 'Cooking is a pation not just a completion of ingeredients together',
        )
        self.article3 = Article.objects.create(
            title="L'informatique",
            author = self.user3,
            created = '2026-05-14T10:30:00Z',
            synopsis = 'Kifach tweli nadi f lma3lomiate',
            content = 'awalan khassk tfhem , t9der thefd walkin dghia ghadi tnssa , dakshi lash ila fhmti rah ghadi thfed mzyaaan',
        )