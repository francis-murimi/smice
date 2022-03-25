from django.db import models
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
# M-pesa Payment models
class MpesaCalls(BaseModel):
    ip_address = models.TextField()
    caller = models.TextField()
    conversation_id = models.TextField()
    content = models.TextField()
    class Meta:
        verbose_name = 'Mpesa Call'
        verbose_name_plural = 'Mpesa Calls'
class MpesaCallBacks(BaseModel):
    ip_address = models.TextField()
    caller = models.TextField()
    conversation_id = models.TextField()
    content = models.TextField()
    class Meta:
        verbose_name = 'Mpesa Call Back'
        verbose_name_plural = 'Mpesa Call Backs'
class MpesaPayment(BaseModel):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    receipt_no = models.CharField(max_length = 15, default='AAA')
    transaction_date = models.CharField(max_length = 20, default='AAA')
    phone_number = models.CharField(max_length = 15, default='AAA')
    used = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Mpesa Payment'
        verbose_name_plural = 'Mpesa Payments'
    def __str__(self):
        return self.receipt_no
