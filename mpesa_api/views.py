from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,get_object_or_404
import requests
from requests.auth import HTTPBasicAuth
import json
from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword
from django.views.decorators.csrf import csrf_exempt
from .models import MpesaPayment
from.forms import TransactionForm
from orders.models import Order
from django.template import loader
from django.views.decorators.http import require_http_methods

def getAccessToken(request):
    consumer_key = 'her3AGkiH3KiaQPBf7lbJJJXiqDGhG4h'
    consumer_secret = 'ANcRGmZw9D969MpP'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)



def lipa_na_mpesa_online(request, id):
    order = get_object_or_404(Order, id=id)
    # converting money from order to integer type
    pesa = order.get_total_cost()
    amount = int(pesa)
    # end
    # converting phone number to integer
    phone = order.phone_number
    simu = int(phone)
    # end
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,
        "PartyA": simu,# replace with your phone number to get stk push
        "PartyB": LipanaMpesaPpassword.Business_short_code,
        "PhoneNumber": simu,  # replace with your phone number to get stk push
        "CallBackURL": "https://3b0486bc3128.ngrok.io/webhooks/example/",
        "AccountReference": "FMurimi",
        "TransactionDesc": "Testing stk push"
    }
    response = requests.post(api_url, json=request, headers=headers)
    #template = loader.get_template('mpesa_api/payment.html')
    return HttpResponse(response)
    #return HttpResponse('success')






