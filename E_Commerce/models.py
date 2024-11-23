from django.db import models
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



# Create your models here

class Order(models.Model):
    # ForeignKey linking to the Customer model
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,  # Delete orders if the associated customer is deleted
        related_name='orders'  # Access orders through customer.orders.all()
    )

    # Automatically set the date and time when an order is created
    order_date = models.DateTimeField(auto_now_add=True)

    # Store the total amount with 10 digits and 2 decimal places
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
         return f"Order #{self.id} by {self.customer.name}"
