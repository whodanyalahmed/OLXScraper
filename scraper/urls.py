from django.urls import path
from .views import homeView,search,minView,maxView,listView,test
urlpatterns = [
    path('',homeView.as_view(),name="home"),
    path('search',search,name="search"),
    path('min',minView.as_view(),name="min"),
    path('max',maxView.as_view(),name="max"),
    path('list',listView.as_view(),name="list"),
    path('test',test,name="test"),
    

    ]
