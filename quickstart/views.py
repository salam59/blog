from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from quickstart.models import Article
from quickstart.serializers import ArticleSerializer
# Create your views here.

class ArticleGenericAPIView(GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    #In generic view there is no need to sendout the content of user and authentication details in the request
    # authentication_classes = [SessionAuthentication,BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "id"

    def get(self,request,id=None):
        if id:
            return self.retrieve(request,id) # single object
        
        return self.list(request) # all objects list
    
    def post(self,request,id=None):
        return self.create(request)
    
    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id):
        return self.destroy(request,id)
    

# class ArticleAPI(APIView):

#     def get(self,request):
#         articles = Article.objects.all()
#         serialize = ArticleSerializer(articles,many = True)
#         return Response(serialize.data)
    
#     def post(self,request):
#         data = request.data
#         serialize = ArticleSerializer(data=data)
#         if serialize.is_valid():
#             serialize.save()
#             return Response(serialize.data)
#         return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)


# class ArticleDetailsAPI(APIView):
#     def get_object(self,id):
#         try:
#             return Article.objects.get(id=id)
#         except:
#             return Response("NOT FOUND",status=status.HTTP_204_NO_CONTENT)
        
#     def get(self,request,id):
#         article = self.get_object(id)
#         serialize = ArticleSerializer(article,many=False)
#         return Response(serialize.data,status=status.HTTP_302_FOUND)
    
#     def put(self,request,id):
#         article = self.get_object(id)
#         data = request.data
#         serialize = ArticleSerializer(article,data=data)
#         if serialize.is_valid():
#             serialize.save()
#             return Response(serialize.data,status=status.HTTP_202_ACCEPTED)
#         return HttpResponse("Data Invalid",status=status.HTTP_304_NOT_MODIFIED)

#     def delete(self,request,id):
#         article = self.get_object(id)
#         article.delete()
#         return HttpResponse("DELETED THE ARTICLE",status=status.HTTP_200_OK)

# @api_view(['GET','POST'])
# def article_list(request):

#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles,many=True)
#         return Response(serializer.data)
    
#     if request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return HttpResponse("Success",status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def article_details(request,id):

#     try:
#         article = Article.objects.get(pk=id)
#     except:
#         return HttpResponse("Not Found",status=404)
    
#     if request.method == "GET":

#         serialize = ArticleSerializer(article,many=False)
#         return Response(serialize.data,status=status.HTTP_202_ACCEPTED)
    
#     elif request.method == "PUT": #UPDATE

#         serialize = ArticleSerializer(article,data=request.data)

#         if serialize.is_valid():
#             serialize.save()
#             return HttpResponse("Successfully updated",status=status.HTTP_201_CREATED)
#         return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST) # if the serialized data doesn't match models fields
    
#     elif request.method == "DELETE":
#         article.delete()
#         return Response("Successfully DELETED",status=status.HTTP_202_ACCEPTED)
#     elif request.method == "POST":
#         return Response("POST Not allowed in this URL. Try with /articles")