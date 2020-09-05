from django.db import models
# Create your models here.

class meatproductcategories(models.Model):
    img = models.ImageField(upload_to='pics',default='Null')
    img_alt = models.CharField(max_length=150)
    heading = models.CharField(max_length=150)
    desc = models.TextField()

class product(models.Model):
    img = models.ImageField(upload_to='pics',default='Null')
    img_alt = models.CharField(max_length=150)
    heading = models.CharField(max_length=150)
    desc = models.TextField()
    cost_price = models.IntegerField()
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    stock = models.IntegerField(default=1)
    fid = models.ForeignKey(meatproductcategories,default=0, on_delete=models.SET_DEFAULT)

class customerorderdetails(models.Model):
    name = models.CharField(max_length=150)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=80)
    address = models.CharField(max_length=200)
    town = models.CharField(max_length=30)
    city = models.CharField(max_length=30, default='Mumbai')
    totalamount = models.IntegerField()
    sid = models.BigIntegerField()
    # orderid = models.ForeignKey(product,default=0, on_delete=models.SET_DEFAULT)

class cartt(models.Model):
    heading = models.CharField(max_length=150)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    sessionid = models.BigIntegerField()

class service(models.Model):
    img = models.ImageField(upload_to='pics',default='Null')
    img_alt = models.CharField(max_length=150)
    heading = models.CharField(max_length=80)
    desc =  models.CharField(max_length=400)
    link = models.CharField(max_length=80)
