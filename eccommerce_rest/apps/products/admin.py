from django.contrib import admin
from apps.products.models import *

# Register your models here.
class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'description') # <== Aquí le estamos diciendo como mostrar la info en el admin de Django

class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

admin.site.register(MeasureUnit, MeasureUnitAdmin)
admin.site.register(CategoryProduct, CategoryProductAdmin)
admin.site.register(Indicator)
admin.site.register(Product)