from django.db import models
from shop.models import Product
from django.contrib.auth.models import User
from home.models import UserProfile
from django.urls import reverse
from phone_field import PhoneField


class Order(models.Model):
    orderer = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length= 12, help_text='use 254xxxxxxx format')
    email = models.EmailField()
    delivery_point = models.CharField(max_length=250,help_text='Building or hostel',default='Manyota')
    area = models.CharField(max_length=100, help_text='e.g V.M,Muranga Town',default='V.M')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    packaged = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return 'Order {}'.format(self.id)
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    def get_absolute_url(self):
        return reverse('orders:order_detail',args=[self.id])
    def get_order_detail(self):
        return reverse('mpesa_api:lipa_na_mpesa_online',args=[self.id])
    def get_order_url(self):
        return reverse('home:order_see',args=[self.id])
    def get_order_update(self):
        return reverse('orders:order_update',args=[self.id])
    def confirm_payment(self):
        return reverse ('orders:payment_confirmation',args=[self.id])
    def delete_order(self):
        return reverse ('orders:delete_order',args=[self.id])
    def packaging(self):
        return reverse ('orders:packaging',args=[self.id])
    def make_delivery(self):
        return reverse ('orders:make_delivery',args=[self.id])

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='order_items',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return '{}'.format(self.id)
    def get_cost(self):
        return self.price * self.quantity