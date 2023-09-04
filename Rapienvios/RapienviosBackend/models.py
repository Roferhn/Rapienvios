from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

# ---User Models--#
class User_Type(models.Model):
    type = models.CharField(max_length=50, null=False)
    status = models.BooleanField(default=True, null=False)

    def __str__(self):
        return self.type

class User(models.Model):
       
    name = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100, null= False)
    email = models.EmailField(unique=True, null=False)
    password = models.TextField(validators=[MinLengthValidator(limit_value=6)], null=False)
    phone = models.CharField(validators=[MinLengthValidator(limit_value=8)], max_length=8, null=False)
    type= models.ForeignKey(User_Type, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.email

# --- Shipping Models---#
class Shipping_Status(models.Model):
    status = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.status

class Shipping_Type(models.Model):
    type = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.type

class Shipping(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shipping_date = models.DateField(null=True,blank=True)
    delivery_date = models.DateField(null=True,blank=True)
    update_date = models.DateField(null=True,blank=True)
    volume = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    weigth = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    type = models.ForeignKey(Shipping_Type, on_delete=models.CASCADE)
    status = models.ForeignKey(Shipping_Status, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.status

class Pricing(models.Model):
    ShippingType = models.ForeignKey(Shipping_Type, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    initial_date = models.DateField()
    final_date = models.DateField()

    def __str__(self):
        return self.price

# ---Package Models---#
class Package(models.Model):
    tracking_num = models.CharField(max_length=100,null=False)
    reception_date = models.DateField()
    packaged_date = models.DateField(null=True,blank=True)
    shipping_id = models.ForeignKey(Shipping, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.type

class Locker(models.Model):
    package_id = models.ForeignKey(Package, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.type