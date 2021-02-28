from django.db import models
from django.utils import timezone
# Create your models here.

class Categorymaster(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)

class Location(models.Model):
    location = models.CharField(max_length = 50, primary_key= True)
    state = models.CharField(max_length = 50)
    country = models.CharField(max_length = 50)
    pincode = models.CharField(max_length = 50)

class Brandmaster(models.Model):
    # sno = models.CharField(max_length=10,primary_key=True)
    brandId = models.CharField(max_length=50,primary_key= True)
    brand = models.CharField(max_length=50)

class PartyAddressBook(models.Model):
    shortCode =models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete = models.PROTECT,null = True)
    phone =  models.DecimalField(max_digits=15, decimal_places=0)
    mobile =  models.DecimalField(max_digits=15, decimal_places=0)
    email = models.CharField(max_length=30)
    fax = models.DecimalField(max_digits=15, decimal_places=0)
    gstIn = models.CharField(max_length=20)
    info = models.CharField(max_length=50)
    customer = models.BooleanField(default=False)
    supplier = models.BooleanField(default=False)
    employee = models.BooleanField(default=False)

class Supplierdetails(models.Model):
    contactID = models.ForeignKey(PartyAddressBook, on_delete=models.PROTECT, null = True)
    supplierType = models.CharField(max_length=50, null= True)
    supplierid = models.CharField(max_length=10,primary_key=True)
    suppliername = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phonenumber = models.DecimalField(max_digits=15, decimal_places=0) 
    mobile = models.DecimalField(max_digits=15, decimal_places=0) 

class Units(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    baseUnit = models.CharField(max_length=50)
    shortCode = models.CharField(max_length=50)
    allowFractions = models.BooleanField( default=False, blank= True)

class Tax(models.Model):
    item = models.CharField(primary_key=True, max_length=50)
    rate = models.DecimalField(max_digits=6, decimal_places=3)
    dateFrom = models.DateField(null = True)
    dateTo = models.DateField(null = True)
    remarks = models.CharField(max_length=50, blank= True)

class TaxCategory(models.Model):
    tax = models.ManyToManyField(Tax, max_length=50)
    hsnCode = models.CharField(max_length=50)
    remarks = models.CharField(max_length=50, blank= True)

class ItemMaster(models.Model):
    itemCode =  models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50, blank = True)
    company = models.CharField(max_length=50, blank = True)
    category = models.CharField(max_length=50, blank= True)
    hsnCode = models.CharField(max_length=50)
    packingQty =  models.DecimalField(max_digits=10, decimal_places=4, blank= True)
    unitRate = models.DecimalField(max_digits=10, decimal_places=4)
    retailItem = models.BooleanField( default=False)
    fastMoving = models.BooleanField( default=False)
    baseUnit = models.ForeignKey(Units, on_delete=models.PROTECT, blank= True)
    recoderLevel = models.DecimalField(max_digits=10, decimal_places=4, blank= True)

# class Materialpurchase(models.Model):
#     suppilerId = models.ForeignKey(Supplierdetails, on_delete=models.CASCADE)
#     productId = models.ForeignKey(ItemMaster, on_delete=models.CASCADE)

class Stock(models.Model):
    productId = models.ForeignKey(ItemMaster, on_delete=models.CASCADE)
    quantityOnHand = models.DecimalField(max_digits=15, decimal_places=0)
    purchaseDate = models.DateField()
    stockLocation = models.ForeignKey(Location, max_length = 50, on_delete = models.PROTECT, null = True)

class Login(models.Model):
    cate = (('admin', 'ADMINISTRATOR'), ('MANAGER', 'MANAGER'),('SALESMAN','SALESMAN'))
    email = models.CharField(max_length=50, primary_key=True, default='')
    password = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=cate)

# class PhoneNumbers(models.Model):
#     contactID =  models.ForeignKey(PartyAddressBook, on_delete=models.PROTECT)
#     shortCode =  models.CharField(max_length=50)
#     phoneType =  models.CharField(max_length=50)
#     phoneNumber = models.DecimalField(max_digits=15, decimal_places=0)

# class EmailAddresses(models.Model):
#     contactID =  models.ForeignKey(PartyAddressBook, on_delete=models.PROTECT)
#     shortCode =  models.CharField(max_length=50)
#     emailType =  models.CharField(max_length=50)
#     email =  models.CharField(max_length=50)
 
# class ExtraAddresses(models.Model):
#     contactID =  models.ForeignKey(PartyAddressBook, on_delete=models.PROTECT)
#     shortCode =  models.CharField(max_length=50)
#     addressType =  models.CharField(max_length=50)
#     address =  models.CharField(max_length=50)
#     pin = models.DecimalField(max_digits=6, decimal_places=0)
#     phone =  models.DecimalField(max_digits=15, decimal_places=0)
    
class Employees(models.Model):
    contactID = models.ForeignKey(PartyAddressBook, on_delete=models.PROTECT)
    employeeType = models.CharField(max_length=50)
    partTime = models.BooleanField( default=False)
    payGrade = models.CharField(max_length=50)
    monthlySalary = models.DecimalField(max_digits=10, decimal_places=4)

# class Customers(models.Model):
#     contactID = models.ForeignKey(PartyAddressBook, on_delete=models.PROTECT, null = True)
#     customerType = models.CharField(max_length=50)

class PurchaseVoucher(models.Model):
    voucherId = models.AutoField(primary_key = True, auto_created = True)
    supplier = models.ForeignKey(Supplierdetails, max_length=502, on_delete = models.PROTECT, null = True)
    reference = models.CharField(max_length=50)
    #igst_purchse = models.BooleanField( default=False)
    invNo = models.IntegerField()
    date = models.DateTimeField( default=timezone.now)
    invDate = models.DateTimeField( default=timezone.now)
    dueDate =models.DateTimeField( default=timezone.now)
    WH = models.DecimalField(max_digits=10, decimal_places=4)
    RT = models.DecimalField(max_digits=10, decimal_places=4)
    mrpRetail = models.DecimalField(max_digits=10, decimal_places=4)
    total = models.DecimalField(max_digits=10, decimal_places=4)
    discount = models.DecimalField(max_digits=10, decimal_places=4)
    otherCharges = models.DecimalField(max_digits=10, decimal_places=4)
    rounding = models.DecimalField(max_digits=10, decimal_places=4)
    paid = models.DecimalField(max_digits=10, decimal_places=4)
    balance = models.DecimalField(max_digits=10, decimal_places=4)
    netAmount = models.DecimalField(max_digits=10, decimal_places=4)

class Purchaseitem(models.Model):
    itemNo = models.CharField(max_length=50)
    voucherno = models.ForeignKey(PurchaseVoucher, on_delete=models.PROTECT)
    itemcode = models.CharField(max_length=50)
    itemname = models.CharField(max_length=50)
    size = models.CharField(max_length=50, blank = True)#to be discussed
    unitRate = models.DecimalField(max_digits=10, decimal_places=4)
    qty = models.DecimalField(max_digits=10, decimal_places=4)
    discount = models.DecimalField(max_digits=10, decimal_places=4)
    discAmt = models.DecimalField(max_digits=10, decimal_places=4)
    taxPct = models.ForeignKey(Tax, on_delete=models.PROTECT) 
    tax = models.DecimalField(max_digits=10, decimal_places=4)
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    total =  models.DecimalField(max_digits=10, decimal_places=4)
    class Meta:
        unique_together = (('itemNo', 'voucherno'))
    
class SalesVoucher (models.Model):
    voucherId = models.AutoField(primary_key = True, auto_created = True)
    types = (('RS', 'Retail Sale'), ('B2B', 'Business to Business'))
    vtype = (('SV', ' Sales Voucher'), ('PV', 'Purchase Voucher'))
    customer = models.CharField(max_length=50)
    address = models.CharField(max_length=50, blank = True)
    tin = models.CharField(max_length=50, blank= True)
    typee = models.CharField(max_length=50, choices=types)
    date = models.DateTimeField( default=timezone.now)
    reference = models.CharField(max_length=50, blank= True)
    total = models.DecimalField(max_digits=10, decimal_places=4)
    discount = models.DecimalField(max_digits=10, decimal_places=4, blank= True)
    rounding = models.DecimalField(max_digits=10, decimal_places=4, blank= True)
    recieved = models.DecimalField(max_digits=10, decimal_places=4, blank= True)
    balance = models.DecimalField(max_digits=10, decimal_places=4, blank= True)
    netAmount = models.DecimalField(max_digits=10, decimal_places=4)

class Voucheritem(models.Model):
    itemNo = models.AutoField(primary_key = True, auto_created = True)
    voucherno = models.ForeignKey(SalesVoucher, on_delete=models.PROTECT)
    itemcode = models.CharField(max_length=50)
    itemname = models.CharField(max_length=50)
    #size = models.CharField(max_length=50, blank= True)
    unit = models.ForeignKey(Units, on_delete = models.CASCADE)
    unitRate = models.DecimalField(max_digits=10, decimal_places=4)
    qty = models.DecimalField(max_digits=10, decimal_places=4)
    #discount = models.DecimalField(max_digits=10, decimal_places=4, blank= True)
    tax = models.DecimalField(max_digits=10, decimal_places=4, blank= True)
    total =  models.DecimalField(max_digits=10, decimal_places=4)
    class Meta:
        unique_together = (('itemNo', 'voucherno'))


class register(models.Model):
    suppiler = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    reference = models.CharField(max_length=50)
    inv_No = models.IntegerField()
    wh = models.DecimalField(max_digits=10, decimal_places=4)
    date = models.DateTimeField( default=timezone.now)
    invDate = models.DateTimeField( default=timezone.now)
    dueDate = models.DateTimeField( default=timezone.now)
    rt = models.DecimalField(max_digits=10, decimal_places=4)
    mrpRetail = models.DecimalField(max_digits=10, decimal_places=4)
    total = models.DecimalField(max_digits=10, decimal_places=4)
    discount = models.DecimalField(max_digits=10, decimal_places=4)
    igst = models.DecimalField(max_digits=10, decimal_places=4)
    otherCharges = models.DecimalField(max_digits=10, decimal_places=4)
    rounding = models.DecimalField(max_digits=10, decimal_places=4)
    paid = models.DecimalField(max_digits=10, decimal_places=4)
    netAmount = models.DecimalField(max_digits=10, decimal_places=4)
    balance = models.DecimalField(max_digits=10, decimal_places=4)
