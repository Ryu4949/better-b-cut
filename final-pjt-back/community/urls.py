from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('article/', views.article_list, name="article_list"),
    path('article/<int:article_pk>/', views.article_detail, name="article_detail"),
    path('article/create_article/', views.create_article, name="create_article"),
    path('article/<int:article_pk>/like/', views.like_article, name="like_article"),
    #comment_list
    path('article/<int:article_pk>/comments/', views.create_comment, name="create_comment"),
    path('article/<int:article_pk>/comments/comment_list/', views.comment_list, name="comment_list"),
    path('article/<int:article_pk>/comments/<int:comment_pk>/', views.comment_detail, name="comment_detail"),
    path('article/<int:article_pk>/comments/<int:comment_pk>/like/', views.like_comment, name="like_comment" ),
    # vote
    path('article/<int:article_pk>/vote/', views.vote),
]
