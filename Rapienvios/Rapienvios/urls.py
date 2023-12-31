"""
URL configuration for Rapienvios project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from RapienviosBackend.views import * 

#---API URL---#
router = DefaultRouter()
router.register(r'api/user', UserViewSet)
router.register(r'api/user_type', User_TypeViewSet)


router.register(r'api/packages', PackageViewSet)


router.register(r'api/shipping', ShippingViewSet)
router.register(r'api/shipping_status', Shipping_StatusViewSet)
router.register(r'api/shipping_type', Shipping_TypeViewSet)
router.register(r'api/pricing', PricingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

]

urlpatterns += router.urls