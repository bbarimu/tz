from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length = 120, verbose_name = 'название')
    description = models.TextField(verbose_name = 'описание')

    def __str__(self):
        return self.title

class TypeOfDish(models.Model):
    title = models.CharField(max_length = 120, verbose_name = 'название')
    description = models.TextField( verbose_name = 'описание')

    def __str__(self):
        return self.title


class ListOfIngrediends(models.Model):
    name = models.CharField(max_length = 120, verbose_name = 'название')
    quantity = models.IntegerField(max_length = 120,default = 1, verbose_name = 'Количество')
    init =  models.CharField(max_length = 120, verbose_name = 'единица измерения')

    def __str__(self):
        return self.name

class Receipes(models.Model):
    title = models.CharField(max_length = 120, verbose_name = 'заголовок')
    description = models.TextField(verbose_name = 'описание')
    created_time = models.DateTimeField(auto_now_add = True)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    category = models.ForeignKey(Category, on_delete = models.PROTECT, null = True)
    type = models.ForeignKey(TypeOfDish, on_delete = models.PROTECT)
    list = models.ManyToManyField(ListOfIngrediends,blank=True,null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'