"""smice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home import views 
from django.conf import settings
from django.conf.urls.static import static
#from mpesa.urls import mpesa_urls

urlpatterns = [
    path('',views.home,name = 'home'),
    path('admin/', admin.site.urls),
    path('online', include(('mpesa_api.urls','mpesa_api'),namespace='mpesa_api')),
    #path('home/', include('home.urls')),
    path('',include(('home.urls','home'),namespace='home')),
    path('',include(('orders.urls','orders'),namespace='orders')),
    path('',include(('shop.urls','shop'),namespace='shop')),
    path('',include(('cart.urls','cart'),namespace='cart')),
    path('webhooks/',include(('webhooks.urls','webhooks'),namespace='webhooks')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
