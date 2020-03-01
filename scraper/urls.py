from django.urls import path
from .views import homeView,search,minView,maxView,listView,listextract,getFile,contactView,aboutView
urlpatterns = [
    path('',homeView,name="home"),
    path('search',search,name="search"),
    path('min',minView.as_view(),name="min"),
    path('max',maxView.as_view(),name="max"),
    path('list',listView.as_view(),name="list"),
    path('getlist',listextract,name="getlist"),
    path('getfile',getFile,name="getfile"),
    path('contact',contactView.as_view(),name="contact"),
    path('about',aboutView,name="about"),
    


    ]
