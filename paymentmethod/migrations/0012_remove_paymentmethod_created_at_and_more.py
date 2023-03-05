# Generated by Django 4.1.7 on 2023-03-03 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentmethod', '0011_rename_requency_recurring_frequency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentmethod',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='paymentmethod',
            name='frequency',
        ),
        migrations.RemoveField(
            model_name='paymentmethod',
            name='interval',
        ),
        migrations.RemoveField(
            model_name='paymentmethod',
            name='plan_id',
        ),
        migrations.RemoveField(
            model_name='paymentmethod',
            name='subscription_id',
        ),
        migrations.AlterField(
            model_name='paymentmethod',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.DeleteModel(
            name='Recurring',
        ),
    ]
