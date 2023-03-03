from rest_framework import serializers
from .models import PaymentMethod, PaymentHistory, Recurring


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['id', 'email', 'amount',
                  'last_four_digits', 'expiration_month', 'expiration_year', 'frequency']


class PaymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentHistory
        fields = ['id', 'user', 'amount', 'date']


class RecurrSerializer(serializers.ModelSerializer):
    payment_method = PaymentMethodSerializer()

    class Meta:
        model = Recurring
        fields = ['id', 'user', 'amount', 'subscription_id', 'plan_id',
                  'status', 'start_date', 'end_date', 'payment_method']

    def create(self, validated_data):
        payment_method_data = validated_data.pop('payment_method')
        payment_method = PaymentMethod.objects.create(**payment_method_data)
        subscription = Recurring.objects.create(
            payment_method=payment_method, **validated_data)
        return subscription

    def update(self, instance, validated_data):
        payment_method_data = validated_data.pop('payment_method')
        payment_method = instance.payment_method
        for key, value in payment_method_data.items():
            setattr(payment_method, key, value)
        payment_method.save()
        instance = super().update(instance, validated_data)
        return instance
