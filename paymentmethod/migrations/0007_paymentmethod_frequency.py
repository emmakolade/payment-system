# Generated by Django 4.1.7 on 2023-03-03 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentmethod', '0006_recurring'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentmethod',
            name='frequency',
            field=models.CharField(blank=True, choices=[('monthly', 'Monthly'), ('weekly', 'Weekly'), ('yearly', 'Yearly')], max_length=10, null=True),
        ),
    ]