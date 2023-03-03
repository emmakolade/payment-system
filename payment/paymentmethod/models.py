from django.db import models
from authentication.models import User


# class PaymentMethod(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     email = models.EmailField()
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     last_four_digits = models.CharField(max_length=4, blank=True, null=True)
#     card_holder_name = models.CharField(max_length=255)
#     expiration_month = models.CharField(max_length=2)
#     expiration_year = models.CharField(max_length=4)
#     cvv = models.CharField(max_length=3)

#     def __str__(self):
#         return self.card_holder_name

class PaymentMethod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    last_four_digits = models.CharField(max_length=4, blank=True, null=True)
    card_holder_name = models.CharField(max_length=255, blank=True, null=True)
    expiration_month = models.CharField(max_length=2, blank=True, null=True)
    frequency = models.CharField(max_length=10, choices=[('weekly', 'Weekly'), (
        'monthly', 'Monthly'), ('yearly', 'Yearly')], blank=True, null=True)

    expiration_year = models.CharField(max_length=4, blank=True, null=True)
    cvv = models.CharField(max_length=3, blank=True, null=True)
    plan_id = models.CharField(max_length=100, blank=True, null=True)
    subscription_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    interval = models.CharField(max_length=10, choices=[(
        'monthly', 'Monthly'), ('weekly', 'Weekly'), ('yearly', 'Yearly')], blank=True, null=True)


class PaymentHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    # status = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user}"


class Recurring(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    # email = models.EmailField()
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    frequency = models.CharField(max_length=10, choices=[('weekly', 'Weekly'), (
        'monthly', 'Monthly'), ('yearly', 'Yearly')], blank=True, null=True)
    # # duration = models.IntegerField()
    # start_date = models.DateTimeField(auto_now_add=True)
    # end_date = models.DateTimeField(null=True, blank=True)
    # status = models.CharField(max_length=20, choices=[(
    #     'active', 'Active'), ('canceled', 'Canceled')])
    # subscription_id = models.CharField(max_length=50)
    # plan_id = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user}"
