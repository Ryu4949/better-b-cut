from turtle import st
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Movie, UserGenrePoint
from django.db.models import Avg, Max, Sum
from community.models import Article
from community.serializers import ArticleListSerializer
# rest_framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
#from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from .serializers import MovieSerializer
import random

# @api_view(['GET'])
# @permission_classes([AllowAny])
# def movie_list(request):
#     search = request.GET.get('search', '')
#     if search:
#         movies = Movie.objects.filter(title__contains=search)
#     else:
#         movies = Movie.objects.all()
#     serializer = MovieSerializer(movies, many=True)
#     if serializer.data:
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#     return Response(data={'error': {'message': '영화정보가 없습니다.'}}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list(request):
    search = request.GET.get('search', '')
    movies = [movie for movie in Movie.objects.all() if ''.join(search.split(' ')) in ''.join(movie.title.split(' '))]
    print(f'검색어: {search}, 결과: {movies}')

    serializer = MovieSerializer(movies, many=True)
    if serializer.data:
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    return Response(data={'error': {'message': '영화정보가 없습니다.'}}, status=status.HTTP_200_OK)


    

@api_view(['GET'])
# 수정 필요 - 접근 
@permission_classes([AllowAny])
def movie_recommendation(request):
    user_points = UserGenrePoint.objects.filter(user_id= request.user.id).values('genre').annotate(total_point = Sum('activity')).order_by('-total_point')
    all_movie = Movie.objects.all()
    
    if user_points:
        recommend_genre = user_points[0].get('genre')
        recommend_movie = Movie.objects.filter(genre__contains=recommend_genre)
        if recommend_movie.count() <3:
            random_movie = random.sample(list(all_movie), k=3)
        else:
            random_movie = random.sample(list(recommend_movie), k=3)
        
    else:
        random_movie = random.sample(list(all_movie), k=3)

    serializer = MovieSerializer(random_movie, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def search(request, movie_pk):
    articles = Article.objects.filter(movie_id=movie_pk)
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)