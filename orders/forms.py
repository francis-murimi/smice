from django import forms
from .models import Order
from urllib import request


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['orderer','paid','delivered','packaged']
        #fields = ['orderer','first_name', 'last_name', 'email','phone_number', 'address','postal_code', 'city']
        #initial = {'orderer':request.user.username}
        #form = ContactForm(initial={'email':'johndoe@coffeehouse.com','name':'John Doe'})
        #(attrs={'placeholder':'Enter your first name'})

class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name','last_name','email','phone_number','delivery_point','area']

class ConfirmationForm(forms.Form):
    transaction_code = forms.CharField()