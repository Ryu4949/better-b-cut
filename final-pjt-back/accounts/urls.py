from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/<username>/', views.profile),
    path('profile/<username>/my_articles/', views.my_articles),
    path('profile/<username>/my_comments/', views.my_comments),
]
