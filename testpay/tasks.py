from celery import shared_task
from django.utils import timezone
from testpay.models import Payment, Wallet, Product
from datetime import datetime, timedelta
from django.utils import timezone
from authentication.models import User
from celery.utils.log import get_task_logger
from celery import Celery
from celery.schedules import crontab
from celery import shared_task
from .models import Payment, Wallet


@shared_task
def charge_wallet():
    payments = Payment.objects.filter(is_recurring=True)
    for payment in payments:
        wallet = Wallet.objects.get(user=payment.user)
        try:
            if wallet.balance >= payment.product.price:
                wallet.balance -= payment.product.price
                wallet.save()
                return "Payment automated successfully"
            else:
                raise ValueError(
                    "Insufficient balance in wallet for user "+str(payment.user.full_name))
        except ValueError as e:
            print("Payment failed:", str(e))
            payment.delete()
# @shared_task
# def charge_wallet():
#     payments = Payment.objects.filter(is_recurring=True)
#     for payment in payments:
#         wallet = Wallet.objects.get(user=payment.user)
#         if wallet.balance >= payment.product.price:
#             wallet.balance -= payment.product.price
#             wallet.save()
#             return {"status": "Payment automated successfully."}
#         else:
#             payment.delete()
# @shared_task
# def charge_wallet(payment_id):
#     payment = Payment.objects.get(id=payment_id)
#     wallet = Wallet.objects.get(user=payment.user)
#     if wallet.balance >= payment.product.price:
#         wallet.balance -= payment.product.price
#         wallet.save()
#         payment.is_recurring = True
#         payment.save()
#     else:
#         payment.delete()
