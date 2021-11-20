from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Category(models.Model):
    name = models.CharField(verbose_name='分类名', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name


class Article(models.Model):
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='标题', max_length=255)
    content = models.TextField(verbose_name='内容')
    author = models.CharField(verbose_name='作者', max_length=255)
    pic = models.ImageField(verbose_name='封面', upload_to='img')

    read_times = models.IntegerField(verbose_name='点击次数', default=0, validators=(MinValueValidator(0), ))
    release_time = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
