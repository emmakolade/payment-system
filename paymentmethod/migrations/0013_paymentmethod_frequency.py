# Generated by Django 4.1.7 on 2023-03-03 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentmethod', '0012_remove_paymentmethod_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentmethod',
            name='frequency',
            field=models.CharField(blank=True, choices=[('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Yearly')], max_length=10, null=True),
        ),
    ]
