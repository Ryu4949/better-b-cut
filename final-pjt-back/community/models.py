from email.policy import default
from django.conf import settings
from django.db import models
import movies.models
import math

# 게시글
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=100)
    movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def result(self):
        results = []
        total_votes = self.votes.count()    #해당 article의 전체 투표수
        if not total_votes: #투표가 없으면 50:50
            results = [50, 50]
        else:
            for choice in self.choices.all():
                if not results:
                    results.append(math.ceil((choice.vote_set.count()/total_votes)*100))  #소수점 버림
                else:
                    results.append(100-results[0])
        return results  


# 게시글 좋아요
class ArticleLikeUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articlelikeusers')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='articlelikeusers')


# 댓글
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    # 대댓글 => reply = models.ForeignKey('self', on_delete = models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


# 댓글 좋아요
class CommentLikeUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='commentlikeusers')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='commentlikeusers')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='commentlikeusers')

# 투표에 대한 선택
class Choice(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='choices')
    content = models.CharField(max_length=100)
    img = models.ImageField(upload_to="image", default="image/")


# 투표 데이터
class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='votes')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='votes')
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    
