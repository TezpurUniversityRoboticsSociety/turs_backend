from django.urls import path,include
from django.conf.urls import url
from django.views.generic import ListView,DetailView
from blog.models import Post
from . import views

urlpatterns = [
	path('',views.register,name='register'),
]