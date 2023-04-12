from datetime import date
from django.db import models

# Create your models here.


class Review(models.Model):
    username = models.CharField(max_length=40)
    user_review = models.TextField()
    ratings = models.IntegerField()


# this is for sharing users memory from our hotel serviecs....
# currently this image folder we do for sqlite folder but if we want then we can further upgrade it for different database as we do for hotellist model...
# if we create a new table then we dont have to give default values but if we make some changes in a table then we have to give default values to those new fields which we add during modification to the table.......
class Memory(models.Model):
    username = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    image = models.FileField(upload_to="user_memories/",max_length=2500, null=True, default=None)
    about = models.TextField()
    date = models.DateField(default=date.today)
