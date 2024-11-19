from django.db import models

# Create your models here.

#The relationship between Customer to Order is a One-Many relationship given that one customer can have multiple orders but each order can belong to one customer.The foreign Key is in the order Model thus linking it to the customer model
#name- the full name of the customer
#email- a unique field that identifies customers by their email address
class Customer(models.Model):
    name=models.CharField(max_length=255) #Customer's name
    email=models.EmailField(unique=True)  #Customer's email should be unique

    def __str__(self):
       return self.name
    