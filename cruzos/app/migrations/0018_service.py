# Generated by Django 3.0.8 on 2020-09-04 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_product_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='Null', upload_to='pics')),
                ('img_alt', models.CharField(max_length=150)),
                ('heading', models.CharField(max_length=80)),
                ('desc', models.CharField(max_length=400)),
                ('link', models.CharField(max_length=80)),
            ],
        ),
    ]