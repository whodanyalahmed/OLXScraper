from django.urls import path
from .views import homeView,search
urlpatterns = [
    path('',homeView.as_view(),name="home"),
    path('search',search,name="search")
    ]
