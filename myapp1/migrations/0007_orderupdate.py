# Generated by Django 3.1.5 on 2021-03-30 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0006_auto_20210130_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
