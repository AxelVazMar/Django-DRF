from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.users.views import Login, Logout, UserToken

schema_view = get_schema_view(
    openapi.Info(
        title='API Documentation',
        default_version='v0.1',
        description="Public API documentation of the Eccomerce",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', Login.as_view(), name = 'Login'), # las '' representan la página por defecto, así que ahí estará nuestro endpoint de inicio de sesión
    path('logout/', Logout.as_view(), name = 'Logout'),
    path('admin/', admin.site.urls),
    path('user/', include('apps.users.api.urls')),
    path('refresh-token/', UserToken.as_view(), name='refresh_token'),
    # path('products/', include('apps.products.api.urls')) <== de esta manera products/ se enlaza a urls
    path('products/', include('apps.products.api.routers')), # <== enlazando a routers
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
