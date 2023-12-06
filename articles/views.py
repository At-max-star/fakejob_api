from .models import Article
from .serializers import ArticleSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics

class ArticleCreateView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetailView(APIView):
    def post(self, request, *args, **kwargs):
        article_id = request.data.get('article_id', None)
        if article_id is not None:
            try:
                article = Article.objects.get(id=article_id)
                serializer = ArticleSerializer(article)
                return Response(serializer.data)
            except Article.DoesNotExist:
                return Response({"error": "Article not found"}, status=404)
        return Response({"error": "article_id is required"}, status=400)