from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets,response,status
from boon.models import *
import boon.serializer as ser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import api_view, permission_classes
# Create your views here.
import logging, os, json

# def brandmasterCheck(request):
#     if request.method == 'POST':
        
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             responseData['flag']="1"
#             return HttpResponse(content=json.dumps(responseData),content_type="application/json",status=200)
#         else:
#             responseData['flag']="0"
#             return HttpResponse(content=json.dumps(responseData),content_type="application/json",status=200)

@api_view(['GET'])
@permission_classes([AllowAny])
def itemCheck(request):
    #logging.info()
    item = ItemMaster.objects.filter(itemCode=request.GET.get("itemCode")).first()
    if item:
        reply= {}
        reply['itemname'] = item.name
        reply['unitrate'] = float(item.unitRate)
        reply['tax'] = taxCalculation(item.hsnCode, item.unitRate)
        return HttpResponse(json.dumps(reply), status= status.HTTP_200_OK)
    else:
        return HttpResponse("No items found", status = status.HTTP_204_NO_CONTENT)

#-------------------------TAX CALCULATION--------------------------------------
def taxCalculation(hsn, amt):
    taxCat = TaxCategory.objects.filter(hsnCode = hsn).first()
    reply = {}
    res = {}
    taxList = {}
    totAmt = 0
    taxPer = 0
    if taxCat:
        for dept in taxCat.tax.all():
            reply[dept.item] = str(dept.rate)
        for key, value in reply.items():
            amount = float(amt) * float(value)/100
            taxList[key] = amount
            totAmt = totAmt + amount
            taxPer = taxPer + float(value)
        res['Amount'] = totAmt
        res['percentage'] = taxPer
        return res
#--------------------------------------------------------------------------------


class CategorymasterViewSet(viewsets.ModelViewSet):
    queryset = Categorymaster.objects.all().order_by('-sno')
    serializer_class = ser.CategorymasterSerializer

class BrandmasterViewSet(viewsets.ModelViewSet):
    queryset = Brandmaster.objects.all().order_by('-brandId')
    serializer_class = ser.BrandmasterSerializer
  
class ItemMasterViewSet(viewsets.ModelViewSet):
    queryset = ItemMaster.objects.all().order_by('-itemCode')
    serializer_class = ser.ItemmasterSerializer

class TaxViewSet(viewsets.ModelViewSet):
    queryset = Tax.objects.all().order_by('-item')
    serializer_class = ser.TaxSerializer

class TaxCategoryViewSet(viewsets.ModelViewSet):
    queryset = TaxCategory.objects.all().order_by('-hsnCode')
    serializer_class = ser.TaxCategorySerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('-location')
    serializer_class = ser.LocationSerializer

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Units.objects.all().order_by('-name')
    serializer_class = ser.UnitSerializer

class SupplierdetailsViewSet(viewsets.ModelViewSet):
    queryset = Supplierdetails.objects.all().order_by('-supplierid')
    serializer_class = ser.SupplierdetailsSerializer

class SalesVoucherViewSet(viewsets.ModelViewSet):
    queryset = SalesVoucher.objects.all().order_by('-voucherId')
    serializer_class = ser.SalesVoucherSerializer

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = PurchaseVoucher.objects.all().order_by('-voucherId')
    serializer_class = ser.PurchaseVoucherSerializer

class VoucherItemViewSet(viewsets.ModelViewSet):
    queryset = Voucheritem.objects.all().order_by('-voucherno')
    serializer_class = ser.VoucherItemSerializer

class PartyAddressBookViewSet(viewsets.ModelViewSet):
    queryset = PartyAddressBook.objects.all().order_by('-name')
    serializer_class = ser.PartyAddressBookSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all().order_by('-productId')
    serializer_class = ser.StockSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all().order_by('-contactID')
    serializer_class = ser.EmployeesSerializer