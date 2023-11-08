# Generated by Django 4.2.4 on 2023-09-01 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Tamil Nadu', 'Tamil Nadu'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Telangana', 'Telangana'), ('Maharashtra', 'Maharashtra'), ('New Delhi', 'New Delhi'), ('West Bengal', 'West Bengal'), ('Goa', 'Goa'), ('Puducherry', 'Puducherry')], max_length=100),
        ),
    ]
