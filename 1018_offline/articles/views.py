from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .serializers import ArticleListSerializer, ArticleSerializer
from .models import Article


@api_view(['GET', 'POST',])
def article_list_or_create(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        # articles = get_list_or_404(Article)
        articles = Article.objects.order_by('-pk')
        
        serialize = ArticleListSerializer(articles, many=True)
        
        return Response(serialize.data)
    else:
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','DELETE','PUT',])
def article_detail_or_delete_or_update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response({'delete': f'{article_pk}번 게시글 삭제'},
                        status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = ArticleSerializer(article, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)