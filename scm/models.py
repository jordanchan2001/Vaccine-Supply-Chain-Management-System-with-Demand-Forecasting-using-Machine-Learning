from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
import uuid
import hashlib

User = get_user_model()

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    id_user = models.IntegerField()
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    profileimg = models.ImageField(upload_to='profile_images',default='blank-profile-picture.png')
    status = models.CharField(max_length=100, default="Inactive")
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

class Vaccine(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    name = models.CharField(max_length=100)
    disease = models.CharField(max_length=200)
    dosage = models.IntegerField()
    
    def __str__(self):
        return self.name

class Cart(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default = False)
    

class CartItems(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitems',null=True,blank=True)
    vaccine_name = models.CharField(max_length=100)
    vaccine_quantity = models.IntegerField()

class SupplyChain(models.Model):
    id = models.AutoField(primary_key=True)
    ownership = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True,blank=True)
    time_created = models.DateTimeField(default=timezone.now) 
    origin = models.CharField(max_length=100)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    status_transferring = models.BooleanField(default = False)
    issue = models.BooleanField(default = False)
    
class Shipment(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100 , default= 'N/A')
    time_shipment = models.DateTimeField(null=True,blank=True)
    supply_chain = models.ForeignKey(SupplyChain, on_delete=models.CASCADE,null=True, blank=True)
    status = models.CharField(max_length=100 , default='N/A')
    hash = models.CharField(max_length = 1000, default = uuid.uuid1().hex)
    previous_hash = models.CharField(max_length=64,blank=True)