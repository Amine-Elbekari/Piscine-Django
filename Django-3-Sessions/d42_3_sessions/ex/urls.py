from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Upvotes/<int:tip_id>', views.Upvotes, name="upvotes"),
    path('Downvotes/<int:tip_id>', views.Downvotes, name="downvotes"),
    path('Remove/<int:tip_id>', views.RemoveTip, name="removetip"),
    path('registration/', views.Registration.as_view(), name='signup'),

]
