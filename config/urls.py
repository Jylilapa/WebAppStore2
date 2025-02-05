from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [path("admin/", admin.site.urls),
               path("", include("catalog.urls", "catalog")),
               path("", include("blog.urls", "blog"))
               ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
