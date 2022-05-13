# Generated by Django 3.2 on 2022-04-23 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logo')),
                ('favIcon', models.ImageField(upload_to='FavIcon')),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('phone2', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.TextField(blank=True, max_length=200, null=True)),
                ('maps', models.CharField(blank=True, max_length=200, null=True, verbose_name='google map')),
                ('twitter', models.URLField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('youtoube', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('pinterest', models.URLField(blank=True, null=True)),
            ],
        ),
    ]