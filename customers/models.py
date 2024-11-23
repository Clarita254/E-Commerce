from django.db import models

# Create your models here.
# Create your models here.


#The relationship between customer and order is that one customer can have many orders (One-Many relationship)
class Customer(models.Model):#The customer model represents customer entity


    name=models.CharField(max_length=255) #Name of the customer

    email=models.EmailField(unique=True) #The email of the customer should e unique

    def __str__(self):
       return self.name
    
#..........................................................................................................#
#Order model represents an order placed by the customer
#It has a one-many relationship:Each order belongs to one Customer
#The foreign key establishes a link between the order model and the customer model

