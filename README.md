# blog
REST Framework

Serializer-> Model Serializer
Parser and Render --> JsonParser, JsonRender
Response --> HttpResponse, JsonResponse 
Http Requests - GET POST PUT DELETE
CRUD operations
API_View Decorator --> replaces (HttpResponse, JsonResponse) with Response 
                  -->  no need to parse or render data, (JsonParser, JsonRender) replaces with request.data and Response
                  --> we can use status code by importing from rest_framework
