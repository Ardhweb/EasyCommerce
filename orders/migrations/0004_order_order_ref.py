# Generated by Django 3.2 on 2021-04-23 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_ref',
            field=models.CharField(blank=True, default='', max_length=120),
        ),
    ]
