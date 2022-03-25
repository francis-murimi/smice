from django.urls import path
from . import views

app_name = 'mpesa_api'
urlpatterns = [
    path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    path('online/lipa<int:id>', views.lipa_na_mpesa_online, name='lipa_na_mpesa_online'),
]