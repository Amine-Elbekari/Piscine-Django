from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class CustomUser(AbstractUser):
#     pass
class Article(models.Model):

    title = models.CharField(max_length=64, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # i can set models.PROTECT if i want to prevent losing articles by deleting user.
    created = models.DateTimeField(auto_now_add=True, null=False)
    synopsis = models.CharField(max_length=312, null=False)
    content = models.TextField(null=False)
    
    def __str__(self):
        return self.title

class UserFavouriteArticle(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    
    def __str__(self):
        self.article.title
    
