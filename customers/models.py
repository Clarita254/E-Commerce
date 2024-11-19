from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=255) #Customer's name
    email=models.EmailField(unique=True)  #Customer's email should be unique

    def __str__(self):
       return self.name
    