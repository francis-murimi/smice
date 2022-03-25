from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('create/',views.order_create,name='order_create'),
    path('admin/order/<order_id>/',views.admin_order_detail, name='admin_order_detail'),
    path('admin/order/<order_id>/pdf/',views.admin_order_pdf,name='admin_order_pdf'),
    path('order_update/<order_id>/',views.order_update,name='order_update'),
    path('payment/<order_id>/',views.payment_confirmation,name='payment_confirmation'),
    path('dlt/<order_id>/',views.delete_order,name='delete_order'),
    path('order-processing/',views.order_processing,name='order_processing'),
    path('packaging/<order_id>/',views.packaging,name='packaging'),
    path('order-delivery/',views.order_delivery,name='order_delivery'),
    path('delivering/<order_id>/',views.make_delivery,name='make_delivery'),
]
""" url(r'^create/$',views.order_create,name='order_create'),
url(r'^admin/order/(?P<order_id>\d+)/$',views.admin_order_detail,name='admin_order_detail'),
url(r'^admin/order/(?P<order_id>\d+)/pdf/$',views.admin_order_pdf,name='admin_order_pdf'),"""