from django.db import models
from django.contrib.auth.models import User

category = (
    ("Stationary", "Stationary"),
    ("Electronics", "Electronics"),
    ("Food","Food"),
    ("Furniture","Furniture"),
    ("Clothing","Clothing"),
)

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, null =True)
    category = models.CharField(max_length=20, choices=category,null=True)
    quantity = models.PositiveIntegerField(null=True)
    sku = models.CharField(max_length=50,null=True)
    supplier = models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return f'{self.name}-{self.quantity}'
    
class inbound_order(models.Model):
    reference = models.CharField(max_length=50,null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    quantity = models.PositiveSmallIntegerField(null=True)
    date = models.DateField(null=True)
    sku = models.CharField(max_length=50,null=True)
    location = models.CharField(max_length=50,null=True)
    remarks = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return f'{self.product}-{self.staff.username}'
    
    class Meta:
        verbose_name_plural = "Inbound Orders"
    
class outbound_order(models.Model):
    reference = models.CharField(max_length=50,null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    quantity = models.PositiveSmallIntegerField(null=True)
    date = models.DateField(null = True)
    destination = models.CharField(max_length=50,null=True)
    remarks = models.CharField(max_length=100,null=True,blank=True)
    sku = models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return f'{self.product}-{self.staff.username}'

    class Meta:
        verbose_name_plural = "Outbound Orders"