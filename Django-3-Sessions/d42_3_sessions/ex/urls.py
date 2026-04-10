from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Votes/<int:tip_id>', views.Votes, name="votes"),
    path('Remove/<int:tip_id>', views.RemoveTip, name="removetip"),
    path('registration/', views.Registration.as_view(), name='signup'),

]
