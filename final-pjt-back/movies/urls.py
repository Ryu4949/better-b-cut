from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, name="movie_list"),
    path('recommend/', views.movie_recommendation, name="movie_recommendation"),
    path('<int:movie_pk>/search/', views.search, name="search"),
]
