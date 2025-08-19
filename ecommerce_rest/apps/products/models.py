from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel

class MeasureUnit(BaseModel):
    
    description = models.CharField('Descripción', max_length=50, blank=False, null=False, unique=True)
    histroical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value    
    
    class Meta:
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medidas'
    
    def __str__(self):
            return self.description

class CategoryProduct(BaseModel):
    description = models.CharField('Descripción', max_length=50, unique=True, blank=False, null=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
            return self.description    

    class Meta:
        verbose_name = 'Categoría del Producto'
        verbose_name_plural = 'Categorías de los Productos'       

class Indicator(BaseModel):

    descount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Indicador de Oferta')
    historical = HistoricalRecords() 

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return f'Oferta de la Categoría{self.category_product}: %{self.descount_value}'     

    class Meta:
        verbose_name = 'Indicador de Oferta'
        verbose_name_plural = 'Indicadores de Ofertas'

class Product(BaseModel):
    
    name = models.CharField('Nombre del Producto',max_length=150, unique=True, blank=False, null=False)
    description = models.TextField('Descripción del Producto', blank=False, null=False)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de Medida', null = True)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Categoría del Producto', null = True)
    image = models.ImageField('Imagen del Producto', upload_to='products/', blank=True, null=True)
    historical = HistoricalRecords() 

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name