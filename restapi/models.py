from django.db import models

class App(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    appUrl = models.CharField(max_length=500)
    appTitle = models.CharField(max_length=20)
    appMainImage = models.CharField(max_length=50)

class MainCategory(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    app = models.ForeignKey(App,on_delete=models.CASCADE)

class MainSubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    mainSubCategory = models.ForeignKey(MainCategory,on_delete=models.CASCADE)
    description = models.CharField(max_length=500)

class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    mainSubCategory = models.ForeignKey(MainSubCategory,on_delete=models.CASCADE, related_name="subcategories")
    imagesUrl = models.CharField(max_length=500)
    imagesTitle = models.CharField(max_length=20)
    imagesDescription = models.CharField(max_length=50)


