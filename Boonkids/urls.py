"""Boonkids URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include

from rest_framework import routers
from boon import views

router = routers.DefaultRouter()
router.register(r'supplierdetails', views.SupplierdetailsViewSet)
router.register(r'Categorymaster', views.CategorymasterViewSet)
router.register(r'Brandmaster', views.BrandmasterViewSet)
router.register(r'ItemMaster', views.ItemMasterViewSet)
router.register(r'Unit', views.UnitViewSet)
router.register(r'Taxmaster', views.TaxViewSet)
router.register(r'Location', views.LocationViewSet)
router.register(r'PartyAddressBook', views.PartyAddressBookViewSet)
router.register(r'Supplierdetails', views.SupplierdetailsViewSet)
router.register(r'Stock', views.StockViewSet)
router.register(r'Employees', views.EmployeeViewSet)
router.register(r'Taxcategory', views.TaxCategoryViewSet)
router.register(r'VoucherItem', views.VoucherItemViewSet)
router.register(r'SalesVoucher', views.SalesVoucherViewSet)
router.register(r'PurchaseVoucher', views.PurchaseViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', views.login),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('checkItem/', views.itemCheck),
   # path('SalesVoucher/', views.saveSaleVoucher)
]
