from django.contrib import admin
from .models import meatproductcategories
from .models import product
from .models import customerorderdetails
from .models import cartt
from .models import service
# Register your models here.

admin.site.register(meatproductcategories)
admin.site.register(product)
admin.site.register(customerorderdetails)
admin.site.register(cartt)
admin.site.register(service)