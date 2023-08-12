from django.urls import path

from quickstart.views import (
    article_list,
    article_details
)

urlpatterns = [
    path("articles/",article_list,name="articles"),
    path("articles/<int:id>",article_details,name="article-details"),
]