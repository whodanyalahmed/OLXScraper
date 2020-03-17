from django.urls import path
from .views import suchomeView,search,minView,maxView,listView,listextract,getFile,contactView,aboutView,HomeView
urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('home',suchomeView,name="suchome"),
    path('search',search,name="search"),
    path('min',minView.as_view(),name="min"),
    path('max',maxView.as_view(),name="max"),
    path('list',listView.as_view(),name="list"),
    path('getlist',listextract,name="getlist"),
    path('getfile',getFile,name="getfile"),
    path('contact',contactView.as_view(),name="contact"),
    path('about',aboutView,name="about"),



    ]
