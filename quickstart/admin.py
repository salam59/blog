from django.contrib import admin

from quickstart.models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title','author']
    search_fields = ['title','author']
    
admin.site.register(Article,ArticleAdmin)