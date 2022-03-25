from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('product_list',views.product_list,name='product_list'),
    path('<category_slug>/',views.product_list,name='product_list_by_category'),
    path('<int:id>/<slug>/',views.product_detail,name='product_detail'),

]
"""url(r'^$', views.product_list, name='product_list'),
url(r'^(?P<category_slug>[-\w]+)/$',views.product_list,name='product_list_by_category'),
url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.product_detail,name='product_detail'),"""
"""url('',views.product_list,name='product_list'),
url('<category_slug>/',views.product_list,name='product_list_by_category'),
url('<int:id>/<slug>/',views.product_detail,name='product_detail'),"""