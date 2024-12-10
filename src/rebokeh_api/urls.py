from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.documentation import include_docs_urls

from django.contrib import admin

schema_view = get_schema_view(
    openapi.Info(
        title="Rebokeh WebAPI",
        default_version='v1',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    authentication_classes=[],
)

swagger = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("accounts/", include("rest_framework.urls")),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("docs/", include_docs_urls(title="Sanitas WebAPI"),),
]


endpoints = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
]

urlpatterns = swagger + endpoints