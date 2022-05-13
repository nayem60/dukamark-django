# Generated by Django 3.2 on 2022-03-24 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(choices=[('processing', 'processing'), ('Accepted', 'Accepted'), ('OnShipping', 'OnShipping'), ('delivered', 'delivered'), ('canceled', 'canceled')], default='processing', max_length=10)),
                ('code', models.CharField(editable=False, max_length=5)),
                ('tax', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=12)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=12)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('country', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=20)),
                ('zipcode', models.CharField(max_length=50)),
                ('order_note', models.TextField(blank=True, max_length=100, null=True)),
                ('shipping_defferent', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_type', models.CharField(choices=[('Cash On Delivery', 'Cash On Delivery'), ('PayPal', 'PayPal'), ('SSLcomerz', 'SSLcomerz')], default='Cash On Delivery', max_length=100)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.order')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=12)),
                ('status', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
