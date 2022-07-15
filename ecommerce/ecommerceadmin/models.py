from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class product(models.Model):
    productimage = models.ImageField(upload_to='images/')
    productname = models.CharField(max_length=50)
    productprice = models.IntegerField()
    status = models.BooleanField(default=True)

class buy(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=500)
    productid = models.ForeignKey(product,on_delete=models.CASCADE)
    userid = models.ForeignKey(User,on_delete=models.CASCADE)