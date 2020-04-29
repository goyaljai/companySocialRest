from django.db import models

class App(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    imagesUrl = models.CharField(max_length=500)
    imagesTitle = models.CharField(max_length=20)
    imagesDescription = models.CharField(max_length=50)

class MainCategory(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    imagesUrl = models.CharField(max_length=500)
    imagesTitle = models.CharField(max_length=20)
    imagesDescription = models.CharField(max_length=50)
    app = models.ForeignKey(App,on_delete=models.CASCADE)

class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    mainCategory = models.ForeignKey(MainCategory,on_delete=models.CASCADE)
    imagesUrl = models.CharField(max_length=500)
    imagesTitle = models.CharField(max_length=20)
    imagesDescription = models.CharField(max_length=50)
