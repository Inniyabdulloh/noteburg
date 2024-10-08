from django.db import models
from django.contrib.auth.models import AbstractUser
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


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = PhoneNumberField()
    age = models.IntegerField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class EmployeeAttendance(models.Model):
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.employee} {self.day}"


class User(AbstractUser):
    staff = models.IntegerField(choices=(
        (1, "hotel"),
        (2, "kitchen"),
        (3, "admin")
    ))

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.staff}"

class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = PhoneNumberField()
    passport = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Food(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField()
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return f"{self.name} {self.price}"


class FoodOrder(models.Model):
    food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.food} ordered by {self.room}-room"


class ShiftKitchen(models.Model):
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.start_time} {self.end_time}"




class BookedRoom(models.Model):
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return self.admin    

