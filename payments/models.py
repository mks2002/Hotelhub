from django.db import models

# Create your models here.


class Paymentdetail(models.Model):
    # this details are bydefault provide by me ..
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    order_no = models.IntegerField()
    total_cost = models.FloatField(default=0.0)
    payment_status = models.CharField(max_length=50, default='paid')
    # this is the email of that user who is currently logged in ...
    useremail = models.CharField(max_length=50, default=None)


#    we dont take any thing from form as form inputs because the form data is handled by paypal integrations.. ....



# if suppose a user cancelled his order then for that situation we have to create one more table in future where we need to store username email and the amount he paid then we have to save them in this table and have to return the money to user after deducting some amount ......