from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.http import require_POST
import json
from django.views.decorators.csrf import csrf_exempt
from types import SimpleNamespace
from mpesa_api.models import MpesaPayment

@require_POST
@csrf_exempt
def example(request):
    todos = request.body
    x = json.loads(todos, object_hook=lambda d: SimpleNamespace(**d))
    r_code = x.Body.stkCallback.ResultCode
    if r_code==0:
        pesa = x.Body.stkCallback.CallbackMetadata.Item[0].Value
        receipt = x.Body.stkCallback.CallbackMetadata.Item[1].Value
        tarehe = x.Body.stkCallback.CallbackMetadata.Item[3].Value
        phone = x.Body.stkCallback.CallbackMetadata.Item[4].Value
        data = str(pesa)+receipt+str(tarehe)+str(phone)
        payment = MpesaPayment(
            receipt_no = receipt,
            phone_number = phone,
            amount = pesa,
            transaction_date = tarehe,
                    )
        payment.save()
        message = {
                    "ResultCode": 0,
                    "ResultDesc": "Success"
                    }
        return JsonResponse(message)
    else:
        #return HttpResponse('cancelled')
        message = {
                    "ResultCode": 0,
                    "ResultDesc": "Success"
                    }
        return JsonResponse(message)