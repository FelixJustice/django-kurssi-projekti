# Generated by Django 3.2.3 on 2021-05-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unitprice',
            field=models.DecimalField(decimal_places=2, default=3, max_digits=5),
        ),
    ]