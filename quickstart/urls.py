from django.urls import path

from quickstart.views import (
    # article_list,
    # article_details,
    # ArticleAPI,
    # ArticleDetailsAPI,
    ArticleGenericAPIView
)

urlpatterns = [
    # path("articles/",article_list,name="articles"),
    # path("articles/",ArticleAPI.as_view(),name="articles"),
    # path("articles/<int:id>",article_details,name="article-details"),
    # path("articles/<int:id>",ArticleDetailsAPI.as_view(),name="article-details"),
    path("articles/api/",ArticleGenericAPIView.as_view(),name="articles-generic-api"),
    path("articles/api/<int:id>/",ArticleGenericAPIView.as_view(),name="article-generic-api-details"),
]