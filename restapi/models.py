from django.db import models

# Create your models here.

class App(models.Model):
    title = models.CharField(max_length=50)
    imagesUrl = models.CharField(max_length=500)
    imagesTitle = models.CharField(max_length=20)
    imagesDescription = models.CharField(max_length=50)

class MainCategory(models.Model):
    title = models.CharField(max_length=50)
    imagesUrl = models.CharField(max_length=500)
    imagesTitle = models.CharField(max_length=20)
    imagesDescription = models.CharField(max_length=50)
    app = models.ForeignKey(App,on_delete=models.CASCADE)

class SubCategory(models.Model):
    mainCategory = models.ForeignKey(MainCategory,on_delete=models.CASCADE)
    imagesUrl = models.CharField(max_length=500)
    imagesTitle = models.CharField(max_length=20)
    imagesDescription = models.CharField(max_length=50)
