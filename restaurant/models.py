import datetime
from django.db import models
# Create your models here.
class Persons(models.Model):
    name = models.CharField(max_length=80)
    phone = models.IntegerField(max_length=13)
    email = models.EmailField()
    persons = models.ManyToManyField('self')
    date = models.DateField(default=datetime.date.today)
    def __str__(self):
        return self.name