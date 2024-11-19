from django.db import models
from .models import Customer

# Create your models here.

#customer-This is a foreign key referring to the customers model
#order_date-This shows when the order is created
#total_amount- stores the total amount from the order and is set to be a decimal field
class Order(models.Model):
    #One-Many relationship:Each order belongs to one customer
    customer=models.ForeignKey(

      Customer,
      on_delete=models.CASCADE, #Deletes orders if associated customer is deleted
      related_name="orders" #allows to retrieve all orders for customer using customer.orders.all()



    )
    order_date=models.DateTimeField(auto_now_add=True) #Automatically sets the date and time when order is created
    total_amount=models.DecimalField(max_digits=10,decimal_places=2) #Stores the total order amount

def __str__(self):
   return f"Order #{self.id} by {self.customer.name}"