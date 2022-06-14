from rest_framework import serializers
from django.contrib.auth import get_user_model

from movies.serializers import MovieSerializer, UserRatingSerializer
from .models import Article, Comment, Choice, Vote, ArticleLikeUser, CommentLikeUser
from movies.models import Movie


User = get_user_model()

# 댓글
class UserSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = User
            fields = ('pk', 'username',)
        
# account > profile에서 사용하는 내가 쓴 댓글 보기       
class CommentSimpleSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Comment
        fields = ('content', 'created_at',)
        read_only_fields = ('content', 'created_at',)





# Article List Read
class ArticleListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)
    # queryset annotate (views에서 채워줄것!)
    comment_count = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    vote_count = serializers.IntegerField(source = "votes.count")
    class Meta:
        model = Article
        fields = ('pk', 'user', 'title', 'movie', 'comment_count', 'like_count', 'vote_count',)
        read_only_fields = ('user', 'movie', 'comment_count', 'like_count', 'vote_count',)

    def get_comment_count(self, instance): #instance = Article
        data = Comment.objects.filter(article__id=instance.id).count()
        return data

    def get_like_count(self, instance): #instance = Article
        data = ArticleLikeUser.objects.filter(article__id=instance.id).count()
        return data




class ChoiceSerializer(serializers.ModelSerializer):
    article = ArticleListSerializer(read_only=True)
    class Meta:
        model = Choice
        fields = ('pk','article', 'content', 'img',)
        read_only_fields = ('pk', 'article', )
    




class ArticleSimpleListSerializer(serializers.ModelSerializer):
    movie_title = serializers.SerializerMethodField()
    class Meta:
        model = Article
        fields = ('pk', 'movie_title', 'title', 'created_at',)

        
    # get_ 은 고정값 , 뒤는 변수명
    def get_movie_title(self, instance): #instance = Article
        data = Movie.objects.filter(id=instance.movie.id).first()
        return data.title


class VoteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    article = ArticleListSerializer(read_only=True)
    class Meta:
        model = Vote
        fields = ('user', 'article', 'choice',)
        read_only_fields = ('user', 'article', 'choice',)


# community > view에서 사용하는 class
class CommentSerializer(serializers.ModelSerializer):    
    user = UserSerializer(read_only=True)
    article = ArticleSimpleListSerializer(read_only=True)
    like_count = serializers.SerializerMethodField()
    now_like = serializers.SerializerMethodField()
    now_vote = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('pk', 'user', 'content', 'article', 'like_count', 'now_like', 'now_vote',)
        read_only_fields = ('pk','user', 'article', 'like_count', 'now_like', 'now_vote' )

    def get_like_count(self, instance):
        data = CommentLikeUser.objects.filter(comment__id=instance.id).count()
        return data
    
    def get_now_like(self, instance):
        return CommentLikeUser.objects.filter(comment__id=instance.id, user__id=instance.user.id).exists()

    def get_now_vote(self, instance):
        return Vote.objects.filter(article_id=instance.article.id, user_id=instance.user.id).exists()


    # Article C, U, D
class ArticleSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)
    comment_count = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    vote_count = serializers.IntegerField(source = "votes.count", read_only=True)
    now_like = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ('pk', 'user', 'title', 'movie', 'choices', 'comments', 'result', 'comment_count', 'like_count', 'vote_count', 'now_like')
        read_only_fields = ('movie', 'comments', 'choices', 'result', 'comment_count', 'like_count', 'vote_count', 'now_like')
    
    def get_comment_count(self, instance): #instance = Article
        data = Comment.objects.filter(article__id=instance.id).count()
        return data

    def get_like_count(self, instance): #instance = Article
        data = ArticleLikeUser.objects.filter(article__id=instance.id).count()
        return data
    
    def get_now_like(self, instance):
        return ArticleLikeUser.objects.filter(article__id=instance.id, user__id=instance.user.id).exists()
