# Generated by Django 3.2 on 2022-03-25 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0003_categorybanner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footerbanner',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product/banner/footer_banner'),
        ),
    ]