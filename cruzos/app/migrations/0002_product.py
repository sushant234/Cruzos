# Generated by Django 3.0.8 on 2020-07-06 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='Null', upload_to='pics')),
                ('img_alt', models.CharField(max_length=150)),
                ('heading', models.CharField(max_length=150)),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('fid', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='app.meatproductcategories')),
            ],
        ),
    ]