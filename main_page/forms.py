from django import forms
from .models import Product,inbound_order, outbound_order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name","category","quantity", "sku","supplier"]
        
class InboundForm(forms.ModelForm):
    class Meta:
        model = inbound_order 
        fields =["reference","date","sku","quantity","location","remarks"]
        widgets = {
            'student_date_of_birth': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            )
        }
        
class OutboundForm(forms.ModelForm):
    class Meta:
        model = outbound_order 
        fields =["reference","date","sku","quantity","destination","remarks"]
        widgets = {
            'student_date_of_birth': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            )
        }