from rest_framework import serializers

from quickstart.models import Article

#Model serializers
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title','author','email']



#NORMAL SERIALIZER JUST LIKE NORMAL FORMS.FORMS
# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=60)
#     author = serializers.CharField(max_length=60)
#     email = serializers.EmailField(max_length=60)
#     date = serializers.DateTimeField()

#     def create(self,validated_data): #validated_data is input from the request i guess
#         return Article.objects.create(validated_data)
    
#     def update(self,instance,validated_data):
#         instance.title = validated_data.get("title",instance.title)
#         instance.author = validated_data.get("author",instance.author)
#         instance.email = validated_data.get("email",instance.email)
#         instance.date = validated_data.get("date",instance.date)
#         instance.save()
#         return instance