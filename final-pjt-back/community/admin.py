from django.contrib import admin
from .models import Article, Comment, Vote, Choice

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Vote)
admin.site.register(Choice)