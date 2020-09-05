# Generated by Django 3.0.8 on 2020-07-06 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='meatproductcategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='Null', upload_to='pics')),
                ('img_alt', models.CharField(max_length=150)),
                ('heading', models.CharField(max_length=150)),
                ('desc', models.TextField()),
            ],
        ),
    ]
