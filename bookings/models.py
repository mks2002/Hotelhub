from django.db import models


# Create your models here.


class Bookinghotel(models.Model):
    # this are the form inputs....
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    contact_no = models.CharField(max_length=13)
    no_people = models.IntegerField()
    no_rooms = models.IntegerField(default=0)
    start = models.DateField(default=None)
    end = models.DateField(default=None)

    # this are the  detail of that user who is currently logged in ...
    username = models.CharField(max_length=30)
    useremail = models.EmailField(max_length=50,default=None)
    userpassword = models.CharField(max_length=30)

    # this are the details of the hotel for which user is currently doing the booking...
    hotelname = models.CharField(max_length=80, default=None)
    city = models.CharField(max_length=60, default=None)
    state = models.CharField(max_length=60, default=None)
    current_cost = models.FloatField(default=0.0)
    payment_status = models.CharField(max_length=50, default='Unpaid')
