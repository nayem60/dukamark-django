# Generated by Django 3.2 on 2022-03-29 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('variant', '0002_auto_20220324_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='subcategory_child',
        ),
        migrations.RemoveField(
            model_name='size',
            name='subcategory_child',
        ),
    ]
