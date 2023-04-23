from django.db import models

# Create your models here.

# this model is for dbsqlite.3 here we store the image into image_folder ....

# this is for default dbsqlite database model ......
class Hotellist(models.Model):
    name = models.CharField(max_length=80)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=60)
    star = models.IntegerField(default=0)
    image = models.FileField(
        upload_to="image_folder/", max_length=2500, null=True, default=None)
    current_cost = models.FloatField()
    delete_cost = models.FloatField()

#_______________________________________________________________________________________________________________


# this is for wamp server mysql database.........
# everything is same here as in the first model we just change the media image directory so that they remain seperate....
# class Hotellist(models.Model):
#     name = models.CharField(max_length=80)
#     city = models.CharField(max_length=40)
#     state = models.CharField(max_length=60)
#     star = models.IntegerField(default=0)
#     image = models.FileField(
#         upload_to="image_folder_mysql_wamp/", max_length=2500, null=True, default=None)
#     current_cost = models.FloatField()
#     delete_cost = models.FloatField()
    
# our wamp server mysql version is only compatible with the django 4.1 version if I use djanog 4.2  or more upgrade version then it it not going to work then we have to upgrade then entire wamp server....    
    
#________________________________________________________________________________________________________________    


# this model is for postgree database here we store the images into another folder inside the media....
# class Hotellist(models.Model):
#     name = models.CharField(max_length=80)
#     city = models.CharField(max_length=40)
#     state = models.CharField(max_length=60)
#     star = models.IntegerField(default=0)
#     image = models.FileField(
#         upload_to="image_folder_postgree/", max_length=2500, null=True, default=None)
#     current_cost = models.FloatField()
#     delete_cost = models.FloatField()
    
 
#__________________________________________________________________________________________________________________   

# for each time when we deal with one type of database we have to comment the rest models otherwise there ia a chance each model is created in each database....    
