from rest_framework import serializers
from .models import Payment, Wallet, Product
from authentication.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'price', 'created_at']


class PaymentSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(
        slug_field='id', queryset=Product.objects.all(), required=True)

    class Meta:
        model = Payment
        fields = ['id', 'product', 'created_at', 'is_recurring']


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['balance']


class FundWalletSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    def create(self, validated_data):
        return validated_data
