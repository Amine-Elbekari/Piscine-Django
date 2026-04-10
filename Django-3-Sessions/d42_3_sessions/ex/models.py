from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager,PermissionsMixin
from django.utils import timezone
# Create your models here.

# class MyManagerUser(BaseUserManager):
    
#     def create_user(self, username, password):
#         if not username:
#             raise ValueError("You must enter username")
#         user = self.model(username=username)
#         user.normalize_username(user)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, username, password):
#         return self.create_user(username, password)
        
        
# class MyCustomUser(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=50, unique=True)
#     email = models.EmailField(blank=True)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
    
#     objects = MyManagerUser()
#     USERNAME_FIELD = 'username'

# class MyManagerUser(BaseUserManager):
    
#     def create_user(self, username, password):
#         if not username:
#             raise ValueError("You must enter username")
#         user = self.model(username=username)
#         user.normalize_username(user)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, username, password):
#         return self.create_user(username, password)
        
        
class MyCustomUser(AbstractUser):

    pass

class ModelTip(models.Model):
    
    content = models.CharField(max_length=150)

    author = models.ForeignKey(
        MyCustomUser,
        on_delete=models.CASCADE,
        # primary_key=True,
        
    )
    date = models.DateField(auto_now_add=True)
    upvotes = models.ManyToManyField(MyCustomUser, related_name="upvoted_tips")
    downvotes = models.ManyToManyField(MyCustomUser, related_name="downvoted_tips")
    
    def  get_upvote_count(self):
        return self.upvotes.count()
    def get_downvote_count(self):
        return self.downvotes.count()
    def get_total_score(self):
        return self.upvotes.count() - self.downvotes.count()

