# Generated by Django 3.2.3 on 2021-05-24 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_product_unitprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unitprice',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=8),
        ),
    ]
