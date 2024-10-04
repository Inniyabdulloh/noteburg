from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Room(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    number = models.IntegerField(unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, null=True)

    def __str__(self):
        return self.number
    

class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = PhoneNumberField()
    passport = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BookedRoom(models.Model):
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return self.admin    

