from django.contrib import admin
from .models import Order, OrderItem
from django.urls import reverse
from django.utils.safestring import mark_safe

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product'] 
    
class OrderAdmin(admin.ModelAdmin):
    @mark_safe
    def order_detail(self):
        return'<a href="{}" > View </a>' .format(reverse('orders:admin_order_detail', args=[self.id]))
        order_detail.allow_tags = True
    @mark_safe    
    def order_pdf(self):
        return '<a href="{}" > PDF </a>'.format(reverse('orders:admin_order_pdf', args=[self.id]))
        order_pdf.allow_tags = True
        order_pdf.short_description = 'PDF bill'

    list_display = ['id', 'first_name', 'last_name', 'email', 'paid','created', 'updated',order_detail,order_pdf]
    list_filter = ['paid','packaged','delivered', 'created', 'updated']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)

