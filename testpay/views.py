from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import PaymentSerializer, PaymentMethodSerializer
from .models import Payment
from .tasks import charge_card

class PaymentCreateView(generics.CreateAPIView):
    serializer_class = PaymentMethodSerializer
    permission_classes = (permissions.IsAuthenticated,)
    # lookup_field = 'id'

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data)


class PaymentMethodEditView(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PaymentMethodSerializer

    def get_object(self):
        return get_object_or_404(Payment, user=self.request.user)


class PaymentHistoryView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)


class PaymentAutomationView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PaymentSerializer

    def post(self, request, *args, **kwargs):
        charge_card.apply_async(args=[request.user.id])
        return Response({"status": "Payment automation started."})


# class PaymentTerminateView(generics.DestroyAPIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     # serializer_class = PaymentSerializer

#     def post(self, request, *args, **kwargs):
#         charge_card.revoke(terminate=True)
#         return Response({"status": "Payment automation terminated"})

# # class PaymentAutomationView(generics.CreateAPIView):
# #     permission_classes = (permissions.IsAuthenticated,)
# #     serializer_class = PaymentSerializer

# #     def post(self, request, *args, **kwargs):
# #         payment = self.serializer_class(data=request.data)
# #         payment.is_valid(raise_exception=True)
# #         charge_card.apply_async(args=[request.user.id])
# #         payment.save(user=request.user)
# #         return Response({"status": "Payment created."})


# # class PaymentDestroyView(generics.DestroyAPIView):
# #     permission_classes = (permissions.IsAuthenticated,)
# #     serializer_class = PaymentSerializer
# #     queryset = Payment.objects.all()

# #     def delete(self, request, *args, **kwargs):
# #         payment = self.get_object()
# #         revoke(payment.task_id)
# #         payment.delete()
# #         return Response({"status": "Payment deleted."})
