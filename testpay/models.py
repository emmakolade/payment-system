from django.db import models
from authentication.models import User

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        return self.product_name


class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,  null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,  null=True, blank=True)
    # amount = models.DecimalField(
    #     max_digits=15, decimal_places=2,  null=True, blank=True)
    is_recurring = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.full_name} paid ${self.amount} for {self.product.product_name}"


# fund wallet
class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.full_name}'s Wallet Balance: ${self.balance}"
