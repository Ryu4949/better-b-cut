from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from community.models import *
from community.serializers import ArticleSimpleListSerializer, CommentSimpleSerializer

from .serializers import ProfileSerializer

User = get_user_model()

@api_view(['GET'])
def profile(request, username):

    if request.user.username !=  username:
        return Response(data={'본인아니면 조회가안됩니다.'})
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)


#내 게시글 보기
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_articles(request, username):
    """
    게시글을 하나만 만들어보고 VIEW 작성
    내가 작성한 게시글 조회하는 로직
    get(user__username=username) # 0개이면 오류
    article.objects.filter(user__username=username) # 0개이면 오류x
    article = request.data.get('article')
    print(article)
    choice = request.data.get('choice')
    print(choice)
    """
    
    # all_view = 더보기 (게시글 전부 보기)
    if request.user.username ==  username:
        is_view = request.GET.get('all_view')
        if is_view:
            articles = Article.objects.filter(user__username=username).order_by('-created_at')
        else: # null 일때
            articles = Article.objects.filter(user__username=username).order_by('-created_at')[:5] # 생성순
        serializer = ArticleSimpleListSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    

@api_view(['POST'])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



# 내 댓글 보기
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_comments(request, username):
    # all_view = 더보기 (댓글 전부 보기)
    if request.user.username ==  username:
        is_view = request.GET.get('all_view')
        if is_view:
            comments = Comment.objects.filter(user__username=username).order_by('-created_at')
        else: # null 일때
            comments = Comment.objects.filter(user__username=username).order_by('-created_at')[:5] # 생성순
        serializer = CommentSimpleSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


