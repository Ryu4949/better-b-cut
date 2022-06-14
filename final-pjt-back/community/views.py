from msilib.schema import ReserveCost
from turtle import st
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from movies.models import Movie, UserGenrePoint

from .models import Article, ArticleLikeUser, Comment, Choice, CommentLikeUser, Vote
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer, ChoiceSerializer, User, VoteSerializer

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
#from rest_framework_jwt.authentication import JSONWebTokenAuthentication



# 모든 게시글 리스트
@api_view(['GET'])
@permission_classes([AllowAny])
def article_list(request):
    if  request.method == 'GET':
        # criteria - 좋아요, 생성순(pk순)
        criteria = request.GET.get('criteria')
        search = request.GET.get('search', '')
        if search:
            articles = [article for article in Article.objects.all() if ''.join(search.split(' ')) in ''.join(article.title.split(' '))]

        elif criteria:
            articles = Article.objects.order_by('-'+criteria)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(data={'result': {'message': '게시물이 없습니다. '}}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_article(request):
    movie_pk = request.data.get('movie_pk') 
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ArticleSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        new_article = serializer.save(movie=movie, user=request.user)
        # choice
        choices = request.data.get('choices') 
        for choice in choices:
            content = choice.get('content')
            img = choice.get('img')
            Choice.objects.create(
                article=new_article,
                content=content,
                img=img
            )

        # point_genre - 추천 알고리즘에 쓰일 point
        for eachgenre in movie.genre.split(' '):
            #print(eachgenre)
            UserGenrePoint.objects.create(
                user = request.user,
                genre = eachgenre,
                activity = 5
            )

        
        #UserGenrePoint(user=request.user).add_point(genres=movie.genre, activity="article")
        #print(UserGenrePoint(user=request.user).get_top_genre())
            
        return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    movie = Movie.objects.get(pk=article.movie_id)
    if request.method == 'GET':
            serializer = ArticleSerializer(article)
            return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        if request.user ==  article.user:
            if request.method == 'PUT':
                is_comment = Comment.objects.filter(article=article).exists()
                is_vote = Vote.objects.filter(article=article).exists()
                if is_comment or is_vote:
                    return Response(data={'error': '수정할 수 없는 게시글입니다.'}, status=status.HTTP_200_OK)
                else:
                    article.title = request.data.get('title')
                    
                    # movie 수정
                    
                    article.movie = movie
                    article.save()
                    # chioce 수정
                    choices = Choice.objects.filter(article=article)
                    for idx, choice in enumerate(choices):
                        choice.content = request.data.get('choices')[idx].get('content')
                        choice.img = request.data.get('choices')[idx].get('img')
                        choice.save()
                    # serializer = ArticleSerializer(article, request.data)
                    # if serializer.is_valid(raise_exception=True):
                    # serializer.save()
                    return Response(data={'result': {'message': '수정되었습니다. '}}, status=status.HTTP_202_ACCEPTED)
            
            
            elif request.method == 'DELETE':
                
                # point_genre - 추천 알고리즘에 쓰일 point
                for eachgenre in movie.genre.split(' '):
                    #print(eachgenre)
                    UserGenrePoint.objects.create(
                        user = article.user,
                        genre = eachgenre,
                        activity = -5
                    )

                article.delete()

                data ={
                    'delete': f'게시글 [{article.title}]이 삭제되었습니다.',
                }
                return Response(data, status=status.HTTP_204_NO_CONTENT)

        return Response(data={'error': '접근 권한이 없습니다.'}, status=status.HTTP_200_OK)
        

@api_view(['POST'])
def like_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article_like_user = ArticleLikeUser.objects.filter(article=article, user=request.user).first()
    if article_like_user:
        article_like_user.delete()
        return Response(data={'meesage': f'게시글 [{article.title}]에 \'좋아요\'가 취소되었습니다.'}, status=status.HTTP_200_OK)
    else:
        ArticleLikeUser.objects.create(
            article=article,
            user=request.user
        )
        return Response(data={'meesage': f'게시글 [{article.title}]에 \'좋아요\'가 되었습니다.'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    movie = get_object_or_404(Movie, pk=article.movie_id)
    serializer = CommentSerializer(data=request.data)
    vote_status = Vote.objects.filter(article_id = article.pk, user_id = request.user.pk).exists()
    if vote_status:
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)

            # point_genre - 추천 알고리즘에 쓰일 point
            for eachgenre in movie.genre.split(' '):
                #print(eachgenre)
                UserGenrePoint.objects.create(
                    user = request.user,
                    genre = eachgenre,
                    activity = 1
                )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        data = {'message': '투표를 완료한 사람만 댓글을 작성할 수 있습니다.'}
        return Response(data, status=status.HTTP_200_OK)


# 댓글 리스트
@api_view(['GET'])
def comment_list(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    #article = Article.objects.get(pk=article_pk)
    is_view = Comment.objects.filter(article=article).exists()
    if is_view:
        article_comments = Comment.objects.filter(article=article).order_by('-created_at')
        serializer = CommentSerializer(article_comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else: # null 일때   
        return Response(data={'meesage': f'아직 댓글이 없습니다.'}, status=status.HTTP_200_OK)



@api_view(['PUT', 'DELETE'])
def comment_detail(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    article = get_object_or_404(Article, pk=article_pk)
    movie = get_object_or_404(Movie, pk=article.movie_id)
    if request.user ==  comment.user:
        if request.method == 'PUT':
            serializer = CommentSerializer(comment, request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        elif request.method == 'DELETE':
            comment.delete()

            # point_genre - 추천 알고리즘에 쓰일 point
            for eachgenre in movie.genre.split(' '):
                #print(eachgenre)
                UserGenrePoint.objects.create(
                    user = comment.user,
                    genre = eachgenre,
                    activity = -1
                )
        
            data = {
                'delete': f'댓글이 삭제되었습니다',
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
    return Response(data={'error': '접근 권한이 없습니다.'}, status=status.HTTP_200_OK)
        


# 댓글 좋아요
@api_view(['POST'])
def like_comment(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment_like_user = CommentLikeUser.objects.filter(article=article, comment=comment, user=request.user).first()
    if comment_like_user:
        comment_like_user.delete()
        return Response(data={'meesage': f'댓글 [{comment.content}]에 \'좋아요\'가 취소되었습니다.'}, status=status.HTTP_200_OK)
    else:
        CommentLikeUser.objects.create(
            article=article,
            comment=comment,
            user=request.user
        )
        return Response(data={'meesage': f'댓글 [{comment.content}]에 \'좋아요\'가 되었습니다.'}, status=status.HTTP_200_OK)



@api_view(['POST'])
def vote(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    movie = get_object_or_404(Movie, pk=article.movie_id)
    user = request.user

    choice = Choice.objects.get(pk=request.data.get('choice'))  #form에서 'choice'에 선택지 id를 담아서 보내줘야함
    if user.votes.filter(article=article).exists():	#이미 해당 게시글에 투표를 했다면
        data = { 'message': '이미 투표를 완료했습니다!'}
        return Response(data, status=status.HTTP_200_OK)
    else:
        vote = Vote(article=article, user=user, choice=choice)
        # point_genre - 추천 알고리즘에 쓰일 point
        for eachgenre in movie.genre.split(' '):
            #print(eachgenre)
            UserGenrePoint.objects.create(
                user = request.user,
                genre = eachgenre,
                activity = 3
            )
        vote.save()
        data = {
            'message': f'[{choice.content}]에 투표하셨습니다!',
        }
        return Response(data, status=status.HTTP_201_CREATED)


