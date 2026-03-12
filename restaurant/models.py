import datetime

from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10,)
    amount = models.IntegerField(default=0)
    checkout_request_id = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}- {self.status}"
class Meal(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='meals/', null=True, blank=True)
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=[
        ('pending','Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ], default='pending')
    notes = models.TextField(blank=True,)
    def __str__(self):
        return f"{self.customer.username}- {self.date}"