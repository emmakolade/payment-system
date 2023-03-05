# class RecurringPaymentView(APIView):
#     permission_classes = [IsAuthenticated]
#     # serializer_class = PaymentMethodSerializer

#     def post(self, request):
#         # serializer = self.serializer_class(data=request.data)
#         # serializer.is_valid(raise_exception=True)
#         payment_method = PaymentMethod.objects.get(user=request.user)
#         amount = payment_method.amount
#         frequency = payment_method.frequency
#         # duration = request.data.get('duration')

#         # create recurring subscription record
#         recurr = Recurring.objects.create(
#             user=request.user, amount=amount, frequency=frequency)
#         url = 'https://api.flutterwave.com/v3/subscriptions'
#         headers = {
#             'Content-Type': 'application/json',
#             'Authorization': 'Bearer FLWSECK-576b78e13005cd32b2a6486b86216ff8-X'
#         }
#         data = {
#             "plan": recurr.id,
#             "customer": {
#                 "email": request.user.email
#             },
#             "start_date": recurr.start_date,
#             "interval": frequency,
#             # "duration": duration,
#             "amount": str(amount),
#             "currency": "NGN",
#             "seckey": "FLWSECK-576b78e13005cd32b2a6486b86216ff8-X"
#         }
#         response = requests.post(url, headers=headers, json=data)

#         if response.status_code == 200:
#             return Response({'message': 'Recurring Payment Initiated successful'}, status=status.HTTP_201_CREATED)
#         else:
#             error = json.loads(response.text)
#             recurr.delete()
#             return Response({'error': error.get('message')}, status=response.status_code)


# class Recurring(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
#     # email = models.EmailField()
#     amount = models.DecimalField(
#         max_digits=10, decimal_places=2, blank=True, null=True)
#     frequency = models.CharField(max_length=10, choices=[('weekly', 'Weekly'), (
#         'monthly', 'Monthly'), ('yearly', 'Yearly')], blank=True, null=True)
#     # # duration = models.IntegerField()
#     # start_date = models.DateTimeField(auto_now_add=True)
#     # end_date = models.DateTimeField(null=True, blank=True)
#     # status = models.CharField(max_length=20, choices=[(
#     #     'active', 'Active'), ('canceled', 'Canceled')])
#     # subscription_id = models.CharField(max_length=50)
#     # plan_id = models.CharField(max_length=50)

#     def __str__(self):
#         return f"{self.user}"
