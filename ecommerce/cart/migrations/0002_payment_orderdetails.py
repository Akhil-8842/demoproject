# Generated by Django 5.1.5 on 2025-02-17 19:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
        ('shop', '0002_alter_product_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('amount', models.IntegerField()),
                ('order_id', models.CharField(max_length=30)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=30)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_items', models.IntegerField()),
                ('address', models.TextField()),
                ('phone', models.BigIntegerField()),
                ('pin', models.IntegerField()),
                ('order_id', models.CharField(max_length=30)),
                ('payment_status', models.CharField(default='Pending', max_length=30)),
                ('delivery_status', models.CharField(default='Pending', max_length=30)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
