from rest_framework import serializers
from .models import *

#---User Serializers---#

class User_TypeSerializar(serializers.ModelSerializer):
    class Meta:
        model = User_Type
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

#--- Package Serializers---#

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'


#--- Shipping Serializers ---#

class Shipping_StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping_Status
        fields = '__all__'

class Shipping_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping_Type
        fields = '__all__'

class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = '__all__'

class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricing
        fields = '__all__'