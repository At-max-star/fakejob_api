from django.urls import path, include
from rest_framework import routers
from .views import ArticleCreateView, ArticleListView, ArticleDetailView

router = routers.DefaultRouter()
#router.register('articles', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('list/', ArticleListView.as_view(), name='article-list'),
    path('detail/', ArticleDetailView.as_view(), name='article-detail'),
]
