from rest_framework import serializers
from .models import Payment, PaymentMethod


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['last_four_digits', 'expiry_month', 'expiry_year', 'cvv']
        # read_only_fields = ['id']


class PaymentSerializer(serializers.ModelSerializer):
    # payment_method = PaymentMethodSerializer()

    class Meta:
        model = Payment
        fields = ['is_recurring', 'amount']
        
