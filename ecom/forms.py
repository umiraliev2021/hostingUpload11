from django import forms
from django.contrib.auth.models import User

from ecom.models import Warehouse, Worker
from . import models


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['address','mobile','profile_pic']


class ProductForm(forms.ModelForm):
    class Meta:
        model=models.Product
        fields=['name','price','description','product_image']


# address of shipment
class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile= forms.IntegerField()
    Address = forms.CharField(max_length=500)


class FeedbackForm(forms.ModelForm):
    class Meta:
        model=models.Feedback
        fields=['name','feedback']


# for updating status of order
class OrderForm(forms.ModelForm):
    class Meta:
        model=models.Orders
        fields=['status']


# for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))


# ================================================== >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 
# ================================================== >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class WarehouseForm(forms.ModelForm):
    class Meta:
        model = models.Warehouse
        fields = ['amount', 'uom', 'description', 'purchase_price', 'selling_price']


class WorkerForm(forms.ModelForm):
    class Meta:
        model = models.Worker
        fields = ['fio', 'start_work', 'work_experience']


class WorkPerformedForm(forms.ModelForm):
   # warehouse = forms.ModelChoiceField(queryset=Warehouse.objects.all(), initial=0)
   # worker = forms.ModelChoiceField(queryset=Worker.objects.all(), initial=0)

    class Meta:
        model = models.WorkPerformed
        fields = ['name', 'product', 'worker', 'start_work', 'finish_work', 'status']


class CalculationForm(forms.ModelForm):
    class Meta:
        model = models.Calculation
        fields = ['worker', 'currency', 'year', 'january', 'february', 'march', 'april', 'may', 'june', 'july',
                  'august', 'september', 'october', 'november', 'december']


class UOMForm(forms.ModelForm):
    class Meta:
        model = models.UnitsOfMeasurement
        fields = ['name',]


class MaterialForm(forms.ModelForm):
    class Meta:
        model = models.Material
        fields = ['amount', 'workPerformed', 'warehouse']
