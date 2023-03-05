from .models import PaymentMethod, PaymentHistory
from django.conf import settings
import requests
import json
import random
import math
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .models import PaymentMethod, PaymentHistory
from .serializers import PaymentMethodSerializer, PaymentHistorySerializer


class PaymentMethodCreateView(generics.CreateAPIView):
    serializer_class = PaymentMethodSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PaymentHistoryListView(generics.ListAPIView):
    serializer_class = PaymentHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PaymentHistory.objects.filter(user=self.request.user)


# class PaymentView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         # Retrieve payment details from database
#         payment_methods = PaymentMethod.objects.filter(user=request.user)

#         # Initiate payment process for each payment method
#         for payment_method in payment_methods:
#             # amount = amount  # Amount to be charged
#             currency = 'NGN'  # Currency of the charge
#             # description = 'Payment for item'  # Description of the charge

#             # Set up the Flutterwave API endpoint and headers
#             url = 'https://api.flutterwave.com/v3/payments'
#             headers = {
#                 'Content-Type': 'application/json',
#                 'Authorization': 'Bearer FLWSECK-576b78e13005cd32b2a6486b86216ff8-X'
#             }
#             # Set up the request data
#             data = {
#                 'tx_ref': f'{payment_method.id}_{int(timezone.now().timestamp())}',
#                 # "tx_ref": ''+str(math.floor(1000000 + random.random()*9000000)),
#                 # 'tx_ref': 'your_transaction_reference_here',
#                 'amount': str(payment_method.amount),
#                 'currency': currency,
#                 'payment_options': 'card',
#                 'redirect_url': 'https://http://localhost:8000/',
#                 'customer': {
#                     'email': payment_method.email,
#                 },
#             }

#             # Send the payment request to Flutterwave
#             response = requests.post(url, headers=headers, json=data)

#             # Check if the payment was successful
#             if response.status_code == 200:
#                 # Create a PaymentHistory record
#                 PaymentHistory.objects.create(
#                     user=request.user,
#                     amount=payment_method.amount,
#                     date=timezone.now(),
#                     status='Paid'
#                 )
#             else:
#                 # Handle the error
#                 error = json.loads(response.text)
#                 return Response({'error': error.get('message')}, status=response.status_code)
#         return Response({'message': 'Payment automation process initiated'})


class RecurringPaymentView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PaymentMethodSerializer

    def post(self, request):
        # Retrieve payment details from database
        payment_methods = PaymentMethod.objects.filter(user=request.user)

        # Initiate payment process for each payment method
        for payment_method in payment_methods:
            # Set up the Flutterwave API endpoint and headers
            url = 'https://api.flutterwave.com/v3/payment-plans'
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer FLWSECK-576b78e13005cd32b2a6486b86216ff8-X'
            }
            # Set up the request data
            data = {
                'name': 'Subscription Plan',
                'amount': str(payment_method.amount),
                'currency': 'NGN',
                'interval': payment_method.frequency,  # 'monthly', 'weekly', or 'yearly'
                # 'duration': payment_method.duration,  # number of intervals
                'seckey': 'FLWSECK-576b78e13005cd32b2a6486b86216ff8-X',
            }

            # Send the payment plan request to Flutterwave
            response = requests.post(url, headers=headers, json=data)

            # Check if the payment plan was successfully created
            if response.status_code == 200:
                plan_id = response.json().get('data', {}).get('id')
                # Save the plan ID to the database
                payment_method.plan_id = plan_id
                payment_method.save()

                # Set up the recurring request data
                subscription_data = {
                    'email': payment_method.email,
                    'amount': str(payment_method.amount),
                    'currency': 'NGN',
                    'payment_options': 'card',
                    'tx_ref': str(math.floor(1000000 + random.random()*9000000)),
                    # 'authorization': payment_method.authorization_code,
                    'plan_id': plan_id,
                }

                # Send the recurring request to Flutterwave
                subscription_response = requests.post('https://api.flutterwave.com/v3/subscriptions',
                                                      headers=headers,
                                                      json=subscription_data)

                # Check if the recurring was successfully created
                if subscription_response.status_code == 200:
                    subscription_id = subscription_response.json().get('data', {}).get('id')
                    # Save the recurring ID to the database
                    payment_method.subscription_id = subscription_id
                    payment_method.save()

                    # Create a PaymentHistory record
                    PaymentHistory.objects.create(
                        user=request.user,
                        amount=payment_method.amount,
                        date=timezone.now(),
                        status='Paid'
                    )
                else:
                    # Handle the error
                    error = json.loads(response.text)
                    return Response({'message': error.get('message')}, status=response.status_code)

                return Response({'message': 'Payment plan created'})
