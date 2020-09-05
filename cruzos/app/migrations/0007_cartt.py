# Generated by Django 3.0.8 on 2020-07-10 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_product_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
    ]