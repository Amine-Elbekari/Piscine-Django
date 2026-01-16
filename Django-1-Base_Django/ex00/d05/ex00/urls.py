from django.urls import path
from . import views
app_name = 'ex00'

urlpatterns = [
    path('', views.markdown_syntax, name='markdown_syntax')
]