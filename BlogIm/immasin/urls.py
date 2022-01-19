from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from .views import HomeView, ArticleDetailView,contact_us, search_venues, allpost, aboutme
from. import views

urlpatterns = [
   path('', HomeView, name="home"),
   path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
   path('contact-us/', contact_us, name="contact-us"),
   path('search_venues', search_venues, name='search-venues'),
   path('allpost', allpost, name='allpost'),
   path('aboutme', aboutme, name='aboutme'),

]


