# Generated by Django 3.2 on 2022-03-29 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20220325_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productspecification',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specification', to='product.product'),
        ),
    ]
