from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import *
from .serializers import *

# Create your views here.

class PackageListview(View):
    
    def get(self, request):
        packages = Package.objects.all()
        serializer = PackageSerializer(packages, many = True)

        data= serializer.data

        return JsonResponse(data, safe=False)