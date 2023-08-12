from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from quickstart.models import Article
from quickstart.serializers import ArticleSerializer
# Create your views here.

@api_view(['GET','POST'])
def article_list(request):

    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return HttpResponse("Success",status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def article_details(request,id):

    try:
        article = Article.objects.get(pk=id)
    except:
        return HttpResponse("Not Found",status=404)
    
    if request.method == "GET":

        serialize = ArticleSerializer(article,many=False)
        return Response(serialize.data,status=status.HTTP_202_ACCEPTED)
    
    elif request.method == "PUT": #UPDATE

        serialize = ArticleSerializer(article,data=request.data)

        if serialize.is_valid():
            serialize.save()
            return HttpResponse("Successfully updated",status=status.HTTP_201_CREATED)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST) # if the serialized data doesn't match models fields
    
    elif request.method == "DELETE":
        article.delete()
        return Response("Successfully DELETED",status=status.HTTP_202_ACCEPTED)
    elif request.method == "POST":
        return Response("POST Not allowed in this URL. Try with /articles")