# Generated by Django 4.1.7 on 2023-03-03 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paymentmethod', '0010_recurring_amount_recurring_requency'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recurring',
            old_name='requency',
            new_name='frequency',
        ),
    ]
