# Generated by Django 3.2 on 2022-04-01 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('variant', '0003_auto_20220329_0806'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='total',
            new_name='price',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='variant.variants'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('pending payment', 'pending payment'), ('On Hold', 'On Hold'), ('Accepted', 'Accepted'), ('Canceled', 'Canceled')], default='pending', max_length=100),
        ),
    ]
