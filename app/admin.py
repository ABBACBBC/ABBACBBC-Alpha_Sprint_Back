from django.contrib import admin

from .models import Article, Category

# Register your models here.


@admin.register(Article)
class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'author')


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', )
