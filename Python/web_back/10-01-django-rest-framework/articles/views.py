from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        # 여러개 받아올때 many = True 사용
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)        
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    # 단일 데이터만 챙겨오니 many 안써도 된다.
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method =='PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        _