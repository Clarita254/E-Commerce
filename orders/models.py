from django.db import models

# Create your models here.
class Order(models.Model):
    customer=models.ForeignKey(

      Customer,
      on_delete=models.CASCADE, #Deletes orders if associated customer is deleted
      related_name="orders" #Allows reverse lookup from Customers to Orders



    )
    order_date=models.DateTimeField(auto_now_add=True) #Automatically sets the date and time when order is created
    total_amount=models.DecimalField(max_digits=10,decimal_places=2) #Stores the total order amount

def __str__(self):
   return f"Order #{self.id} by {self.customer.name}"