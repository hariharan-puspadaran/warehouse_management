# Generated by Django 4.2 on 2023-04-16 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0006_remove_inbound_order_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inbound_order',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='outbound_order',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
