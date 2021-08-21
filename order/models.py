from django.contrib.auth.models import User
from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Order(models.Model):
    IN_PROCESS = "In Process"
    IN_SHIPPING = "In Shipping"
    RECIEVED = "Recieved"
    order_status = [
        (IN_PROCESS, IN_PROCESS),
        (IN_SHIPPING, IN_SHIPPING),
        (RECIEVED, RECIEVED)

    ]

    address = models.TextField()
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    status = models.CharField(choices=order_status, max_length=35, default=IN_PROCESS)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField(default=0)
    # contact_phone_number = PhoneNumberField(null=True,blank=True)
