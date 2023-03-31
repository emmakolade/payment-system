from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import PaymentSerializer, WalletSerializer, FundWalletSerializer, ProductSerializer
from .models import Product, Payment, Wallet
from authentication.models import User


class ProductCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ProductListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)


class PaymentAutomationView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PaymentSerializer

    def post(self, request, *args, **kwargs):
        product_id = self.kwargs['product_id']
        product = get_object_or_404(Product, id=product_id)
        wallet = Wallet.objects.get(user=self.request.user)

        if wallet.balance < product.price:
            return Response({"error": "Insufficient balance in wallet."}, status=status.HTTP_400_BAD_REQUEST)

        payment = Payment.objects.create(
            product=product, user=request.user, is_recurring=True)
        return Response({"status": "Payment made successfully."}, status=status.HTTP_202_ACCEPTED)


class PaymentStopView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PaymentSerializer

    def delete(self, request, *args, **kwargs):
        product_id = self.kwargs['product_id']
        payment = Payment.objects.filter(
            product_id=product_id, user=request.user, is_recurring=True).first()

        if not payment:
            return Response({"error": "No recurring payment found for the given product."}, status=status.HTTP_404_NOT_FOUND)

        payment.is_recurring = False
        payment.save()
        return Response({"status": "Recurring payment stopped."}, status=status.HTTP_204_NO_CONTENT)


class PaymentListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)


class FundWalletView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = FundWalletSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        wallet, created = Wallet.objects.get_or_create(user=self.request.user)
        wallet.balance += serializer.validated_data['amount']
        wallet.save()
        return Response({"status": "Your wallet has been successfully funded. You can now enjoy using your funds for purchases and transactions."})


class WalletBalanceView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = WalletSerializer

    def get_object(self):
        return get_object_or_404(Wallet, user=self.request.user)
