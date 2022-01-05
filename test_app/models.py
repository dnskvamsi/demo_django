from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    salary = models.IntegerField()
