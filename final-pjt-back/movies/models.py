from django.conf import settings
from django.db import models
from django.db.models import Avg, Max, Sum

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateField(null=True, blank=True)
    vote_average = models.FloatField()
    poster_path = models.URLField(null=True, blank=True)
    #article = models.ForeignKey('community.Article', on_delete=models.CASCADE, related_name='movies', null=True)
    genre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title


class UserRating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='userratings')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='userratings')
    rating = models.FloatField(default=0.0) # null 이면 평균낼 수 없음

    class Meta:
        unique_together = (("user", "movie"),)

    def __str__(self):
        return f'{self.movie.title}-{self.user.username}-{self.rating}'


class UserGenrePoint(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='usergenrepoints')
    genre = models.TextField(null=True, blank=True)
    activity = models.IntegerField(default=0)


'''
[추천 알고리즘]

사용자별 활동한 내역(게시글, 댓글, 투표)에 해당되는 장르에 대해
차등으로 포인트를 매겨서
가장 높은 포인트의 장르를 해당 사용자의 선호 장르로 결정

이 선호 장르에서 상위(평점 ghrdms) 랜덤 20개 중 3개를 보여주기


게시글 작성: 5점
투표 참여 : 3점
댓글 작성 : 1점
'''