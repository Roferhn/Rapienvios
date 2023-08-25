from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

# ---User Models--#
class User_Type(models.Model):
    type = models.CharField(max_length=50)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.type

class User(models.Model):
       
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.TextField() #Investigar e implementar hashing
    phone = models.CharField(validators=[MinLengthValidator(limit_value=8)], max_length=8)
    user_type= models.ForeignKey(User_Type, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.type

# --- Shipping Models---#
class Shipping_Status(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status

class Shipping_Type(models.Model):
    type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.type

class Shipping(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    shipping_date = models.DateField()
    delicery_date = models.DateField()
    updated_date = models.DateField()
    shipping_type_id = models.ForeignKey(Shipping_Type, on_delete=models.CASCADE)
    volume = models.DecimalField(max_digits=10, decimal_places=2)
    weigth = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_status_id = models.ForeignKey(Shipping_Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.type

class Pricing(models.Model):
    shipping_status_id = models.ForeignKey(Shipping_Status, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    initial_date = models.DateField()
    final_date = models.DateField()

    def __str__(self):
        return self.type

# ---Package Models---#
class Package(models.Model):
    tracking_num = models.CharField(max_length=100)
    reception_date = models.DateField(null=False)
    packaged_date = models.DateField(null=False)
    shipping_id = models.ForeignKey(Shipping, on_delete=models.CASCADE)

    def __str__(self):
        return self.type

class Locker(models.Model):
    package_id = models.ForeignKey(Package, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.type