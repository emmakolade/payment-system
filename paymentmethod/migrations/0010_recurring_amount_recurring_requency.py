# Generated by Django 4.1.7 on 2023-03-03 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentmethod', '0009_remove_recurring_amount_remove_recurring_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurring',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='recurring',
            name='requency',
            field=models.CharField(blank=True, choices=[('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Yearly')], max_length=10, null=True),
        ),
    ]
