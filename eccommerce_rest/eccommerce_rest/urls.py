from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('apps.users.api.urls')),
    # path('products/', include('apps.products.api.urls')) <== de esta manera products/ se enlaza a urls
    path('products/', include('apps.products.api.routers')) # <== enlazando a routers
]
