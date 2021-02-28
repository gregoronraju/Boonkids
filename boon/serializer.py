from rest_framework import serializers
from boon.models import *



class CategorymasterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categorymaster
        fields = ['sno','name']

class PartyAddressBookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PartyAddressBook
        fields = ['shortCode','name', 'address', 'location', 'phone', 'mobile', 'email', 'fax', 'gstin', 'info', 'customer', 'supplier', 'employee']

class BrandmasterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brandmaster
        fields = ['brandId','brand']

class ItemmasterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ItemMaster
        fields = ['itemCode','name','description','company','category','hsnCode','packingQty','unitRate', 'retailItem', 'fastMoving', 'baseUnit', 'recoderLevel']

class TaxSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tax
        fields = ['item', 'rate', 'dateFrom', 'dateTo', 'remarks']

class VoucherItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Voucheritem
        fields = ['itemNo', 'voucherno', 'itemcode', 'itemname', 'unit', 'unitRate', 'qty', 'tax', 'total']

class TaxCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaxCategory
        fields = ['tax', 'hsnCode', 'remarks']

class SalesVoucherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SalesVoucher
        fields = ['voucherId', 'customer', 'address', 'tin', 'typee', 'date', 'reference', 'total', 'discount', 'rounding', 'recieved', 'balance', 'netAmount']

class PurchaseVoucherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PurchaseVoucher
        #fields = ['voucherId', 'customer', 'address', 'tin', 'typee', 'date', 'reference', 'total', 'discount', 'rounding', 'recieved', 'balance', 'netAmount']

class UnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Units
        fields = ['name', 'baseUnit', 'shortCode', 'allowFractions']

class SupplierdetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supplierdetails
        fields = ['supplierid','suppliername', 'address', 'phonenumber', 'mobile']
        
class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ['location','state', 'country', 'pincode']

class StockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock
        fields = ['productId','quantityOnHand', 'purchaseDate', 'stockLocation']

class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employees
        fields = ['contactID','employeeType', 'partTime', 'payGrade', 'monthlySalary']