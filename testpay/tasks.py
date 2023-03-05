from celery import shared_task
from django.utils import timezone
from testpay.models import Payment
from authentication.models import User
import requests
import json
import random
import math


@shared_task(bind=True)
def charge_card(self, terminate=False):
    payments = Payment.objects.filter(is_recurring=True)
    for payment in payments:
        # Call Flutterwave API to process the payment
        headers = {
            'Authorization': 'Bearer FLWSECK-576b78e13005cd32b2a6486b86216ff8-X',
            'Content-Type': 'application/json'
        }
        payload = {
            'tx_ref': str(math.floor(1000000 + random.random()*9000000)),
            'amount': payment.amount,
            'currency': 'NGN',
            'payment_options': 'card',
            'customer': {
                'email': payment.user.email,
                'name': payment.user.full_name,
            },
            # 'meta': {
            #     'product_name': payment.item_name,
            #     'order_id': payment.order_id
            # },
            'redirect_url': 'https://your-website.com/redirect-url'
        }
        response = requests.post(
            'https://api.flutterwave.com/v3/payments', headers=headers, json=payload)
        if response.status_code == 200:
            payment.is_recurring = True
            payment.save()
        else:
            return {"status": "Payment processing failed."}
    return "Payment processed successfully"


# def charge_card(self, terminate=False):
#     payments = Payment.objects.filter()
#     for payment in payments:
#         if terminate:
#             # Terminate recurring payments
#             payment.is_recurring = False
#             payment.save()
#             continue
#         # Call Flutterwave API to process the payment
#         headers = {
#             'Authorization': 'Bearer FLWSECK-576b78e13005cd32b2a6486b86216ff8-X',
#             'Content-Type': 'application/json'
#         }
#         payload = {
#             'tx_ref': str(math.floor(1000000 + random.random()*9000000)),
#             'amount': payment.amount,
#             'currency': 'NGN',
#             'payment_options': 'card',
#             'customer': {
#                 'email': payment.user.email,
#                 'name': payment.user.full_name,
#             },
#             # 'meta': {
#             #     'product_name': payment.item_name,
#             #     'order_id': payment.order_id
#             # },
#             'redirect_url': 'https://your-website.com/redirect-url'
#         }
#         response = requests.post(
#             'https://api.flutterwave.com/v3/payments', headers=headers, json=payload)
#         if response.status_code == 200:
#             payment.save()
#         else:
#             return {"status": "Payment processing failed."}
#     return "Payment processed successfully"
