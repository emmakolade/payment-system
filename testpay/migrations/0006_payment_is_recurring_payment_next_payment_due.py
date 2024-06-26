# Generated by Django 4.1.7 on 2023-03-30 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testpay', '0005_payment_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='is_recurring',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='payment',
            name='next_payment_due',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
