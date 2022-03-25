from django import forms

class TransactionForm(forms.Form):
    Transaction_Id = forms.CharField(max_length=100,label='Transaction Id')
