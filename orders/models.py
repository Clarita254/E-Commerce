from django.db import models

# Create your models here.
class Order(models.Model):

          customer = models.ForeignKey(
              'Customer',
          on_delete=models.CASCADE, #deletes orders if the associated customer is deleted
          related_name='orders' #Enables accessing  all orders of a customer via customer.order.all()

)

 #Automatically  sets the date and time when an order is created         
order_date=models.DateTimeField(auto_now_add=True)

#Stores the total order amount with of 10 digits and 2 decimal places
total_amount=models.DecimalField(max_digits=10, decimal_places=2)

def __str__(self):
  return f"Order #{self.id} by {self.customer.name}"
 
 

