from django.contrib import admin
from .models import MpesaPayment

class MpesaPaymentAdmin(admin.ModelAdmin):
    list_display = ['receipt_no','phone_number','amount','transaction_date']
    list_filter = ['amount']
    search_fields = ['receipt_no','phone_number']

admin.site.register(MpesaPayment,MpesaPaymentAdmin)