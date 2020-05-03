from django.db import models
from django_currentuser.middleware import (get_current_authenticated_user)

def user_directory_path1(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}/{2}/{3}'.format(get_current_authenticated_user().username, instance.mainSubCategory.description,instance.imagesTitle,filename)

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(get_current_authenticated_user().username, filename)

class App(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    appUrl = models.CharField(max_length=500)
    appTitle = models.CharField(max_length=20)
    #appMainImage = models.CharField(max_length=50)

    appMainImage = models.ImageField(upload_to=user_directory_path)
    def __str__(self):
        return '%s' % self.title

class MainCategory(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    app = models.ForeignKey(App,on_delete=models.CASCADE)
    def __str__(self):
        return '%s' % self.title

class MainSubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    mainSubCategory = models.ForeignKey(MainCategory,on_delete=models.CASCADE)
    description = models.CharField(max_length=500)

    def __str__(self):
        return '%s' % self.description

class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    mainSubCategory = models.ForeignKey(MainSubCategory,on_delete=models.CASCADE, related_name="subcategories")
    #imagesUrl = models.CharField(max_length=500)
    imagesUrl = models.ImageField(upload_to=user_directory_path1)
    imagesTitle = models.CharField(max_length=20)
    imagesDescription = models.CharField(max_length=50)
    def __str__(self):
        return '%s' % self.imagesDescription

class OrderRequests(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=50)

    def __str__(self):
        return 'order for %s with id %s' % (self.item_name,self.item_id)
