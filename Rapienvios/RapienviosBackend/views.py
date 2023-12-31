from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.

#--- User API---#
class User_TypeViewSet(viewsets.ModelViewSet):
    serializer_class = User_TypeSerializar
    queryset = User_Type.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


#---Package API---#

class PackageViewSet(viewsets.ModelViewSet):
    serializer_class = PackageSerializer
    queryset = Package.objects.all()

    @action(detail=False,methods=['GET'])
    def PakcagesByUser(self, resquest, pk=None):
        
        user = 1
        queryset = Package.objects.filter(user=user)
        serializer = PackageSerializer(queryset,many=True)
        return Response(serializer.data)



#--- Shipping API---#
class ShippingViewSet(viewsets.ModelViewSet):
    serializer_class = ShippingSerializer
    queryset = Shipping.objects.all()

class Shipping_StatusViewSet(viewsets.ModelViewSet):
    serializer_class = Shipping_StatusSerializer
    queryset = Shipping_Status.objects.all()

class Shipping_TypeViewSet(viewsets.ModelViewSet):
    serializer_class = Shipping_TypeSerializer
    queryset = Shipping_Type.objects.all()
    
class PricingViewSet(viewsets.ModelViewSet):
    serializer_class = PricingSerializer
    queryset = Pricing.objects.all()