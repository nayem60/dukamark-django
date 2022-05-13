# Generated by Django 3.2 on 2022-03-24 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('coupon_type', models.CharField(choices=[('fixed', 'fixed'), ('percent', 'percent')], max_length=100)),
                ('coupon_valu', models.IntegerField()),
                ('cart_value', models.IntegerField(blank=True, null=True)),
                ('exfail_date', models.DateTimeField(verbose_name='Coupon Exfail Date')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
