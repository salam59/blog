from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

from quickstart.models import Article
from quickstart.serializers import ArticleSerializer
# Create your views here.

@csrf_exempt
def article_list(request):

    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many=True)
        return JsonResponse(serializer.data,safe=False)
    
    if request.method == "POST":
        data = JSONParser().parse(request) 
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return HttpResponse("Success",status=201)
        return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def article_details(request,id):

    try:
        article = Article.objects.get(pk=id)
    except:
        return HttpResponse("Not Found",status=404)
    
    if request.method == "GET":

        serialize = ArticleSerializer(article,many=False)
        return JsonResponse(serialize.data,status=401)
    
    elif request.method == "PUT": #UPDATE

        data = JSONParser().parse(request)
        serialize = ArticleSerializer(article,data=data)

        if serialize.is_valid():
            serialize.save()
            return HttpResponse("Successfully updated",status=201)
        return JsonResponse(serialize.errors,status=400) # if the serialized data doesn't match models fields
    
    elif request.method == "DELETE":
        article.delete()
        return HttpResponse("Successfully DELETED",status=204)
    elif request.method == "POST":
        return HttpResponse("POST Not allowed in this URL. Try with /articles")