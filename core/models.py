from django.db import models
from django.conf import settings

from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

User=settings.AUTH_USER_MODEL

class TimeStampedModel(models.Model):
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateField(auto_now=True)

    class Meta:
        abstract=True

class LocationModel(TimeStampedModel):
    latitude = models.FloatField()
    longitude = models.FloatField()      

class AddressModel(TimeStampedModel):
    address_line1=models.CharField(max_length=255)
    address_line2=models.CharField(max_length=255)
    city=models.CharField(max_length=56)
    state=models.CharField(max_length=56)
    zip=models.CharField(max_length=10)
    country=models.CharField(max_length=56) 
    location = models.ForeignKey(
        LocationModel, on_delete=models.SET_NULL, blank=True, null=True
    )       

class HospitalModel(TimeStampedModel):
    name=models.CharField(max_length=55)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.ForeignKey(AddressModel, on_delete=models.CASCADE) 

    def __str__(self):
        return self.name

class ProfileModel(TimeStampedModel):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=16)
    address=models.ForeignKey(AddressModel,on_delete=models.CASCADE)    

    def __str__(self):
        return self.user

class ContactModel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.IntegerField()
    message = models.TextField()
    subject = models.CharField(max_length=255)
    is_replied = models.BooleanField(default=False)

    def __str__(self):
        return self.name