from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/CustomerProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name


class Product(models.Model):
    name = models.CharField(max_length=40)
    product_image = models.ImageField(upload_to='product_image/', null=True, blank=True)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Orders(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Order Confirmed', 'Order Confirmed'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=500, null=True)
    mobile = models.CharField(max_length=20, null=True)
    order_date = models.DateField(auto_now_add=True, null=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)


class Feedback(models.Model):
    name = models.CharField(max_length=40)
    feedback = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


# ================================================== >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#
# ================================================== >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class UnitsOfMeasurement(models.Model):
    name = models.CharField('Name', max_length=255, blank=False)
    symbol = models.CharField('Symbol', max_length=10, blank=False)

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField('Currency name', max_length=255, blank=False)
    symbol = models.CharField('Symbol', max_length=10, blank=False)
    code = models.CharField('Currency code', max_length=10, blank=True)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    amount = models.CharField(max_length=40)
    uom = models.ForeignKey('UnitsOfMeasurement', on_delete=models.CASCADE, null=True)
    description = models.TextField('описание', blank=True, null=True)
    purchase_price = models.IntegerField('цена покупки', blank=True, null=True)
    selling_price = models.IntegerField('цена продажи', blank=True, null=True)

    def __str__(self):
        return self.description


class Worker(models.Model):
    fio = models.CharField(max_length=255)
    # start_work = models.DateField(auto_now_add=True, null=True)
    start_work = models.DateField('start_work', max_length=255, blank=True, null=True)
    work_experience = models.CharField(max_length=100)
    process_work = models.TextField('process work', blank=True, null=True)
    completed_work = models.TextField('описание', blank=True, null=True)

    def __str__(self):
        return self.fio


class WorkPerformed(models.Model):
    STATUS = (
        ('In progress', 'In progress'),
        ('Completed', 'Completed'),
    )
    name = models.CharField(max_length=255, null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    # warehouse = models.ManyToManyField(Warehouse, verbose_name='Warehouse', blank=True)
    worker = models.ManyToManyField(Worker, verbose_name='Worker', blank=True)
    start_work = models.DateField('start_work', max_length=255, blank=True, null=True)
    finish_work = models.DateField('finish_work', max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)
    # count = models.IntegerField('Count', blank=True, null=True)
    # uom = models.ForeignKey('UnitsOfMeasurement', on_delete=models.CASCADE, null=True)


class Material(models.Model):
    amount = models.CharField(max_length=40)
    workPerformed = models.ForeignKey('WorkPerformed', on_delete=models.CASCADE, null=True, blank=True)
    warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE, null=True)
    # uom = models.ForeignKey('UnitsOfMeasurement', on_delete=models.CASCADE, null=True)


class Calculation(models.Model):

    worker = models.ForeignKey('Worker', on_delete=models.CASCADE, null=True)
    currency = models.ForeignKey('Currency', on_delete=models.CASCADE, null=True)
    year = models.IntegerField('Year', choices=[(r,r) for r in range(1984, datetime.date.today().year+1)], default=datetime.date.today().year)
    # year = models.CharField(max_length=50, null=True, choices=YEAR)
    january = models.IntegerField('January', blank=True, null=True)
    february = models.IntegerField('february', blank=True, null=True)
    march = models.IntegerField('March', blank=True, null=True)
    april = models.IntegerField('April', blank=True, null=True)
    may = models.IntegerField('May', blank=True, null=True)
    june = models.IntegerField('June', blank=True, null=True)
    july = models.IntegerField('July', blank=True, null=True)
    august = models.IntegerField('August', blank=True, null=True)
    september = models.IntegerField('September', blank=True, null=True)
    october = models.IntegerField('October', blank=True, null=True)
    november = models.IntegerField('November', blank=True, null=True)
    december = models.IntegerField('December', blank=True, null=True)
