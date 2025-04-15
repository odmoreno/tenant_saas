from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from a_tenant_manager.admin import tenant_admin_site
from a_home.views import *

urlpatterns = [
    path("admin_tenants/", tenant_admin_site.urls),
    path("", include("a_core.urls")),
]

# Only used when DEBUG=True, whitenoise can serve files when DEBUG=False
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
