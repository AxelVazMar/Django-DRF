from django.contrib import admin
from apps.products.models import *

# Register your models here.
admin.site.register(CategoryProduct)
admin.site.register(MeasureUnit)
admin.site.register(Indicator)
admin.site.register(Product)