"""
Main URL mapping configuration file.

Include other URLConfs from external apps using method `include()`.

It is also a good practice to keep a single URL to the root index page.

This examples uses Django's default media
files serving technique in development.
"""

from django.conf import settings
from django.contrib import admin
from django.contrib.admindocs import urls as admindocs_urls
from django.urls import include, path
from health_check import urls as health_urls

from server.apps.main.api.v1 import urls as api_v1_urls

admin.autodiscover()

urlpatterns = [
    path('api/v1/', include(api_v1_urls, namespace='api_v1_urls')),
    path('health/', include(health_urls)),  # noqa: DJ05
    path('admin/doc/', include(admindocs_urls)),  # noqa: DJ05
    path('admin/', admin.site.urls),
]

if settings.DEBUG:  # pragma: no cover
    import debug_toolbar  # noqa: WPS433
    from django.conf.urls.static import static  # noqa: WPS433

    urlpatterns = [
        # URLs specific only to django-debug-toolbar:
        path('__debug__/', include(debug_toolbar.urls)),  # noqa: DJ05
    ] + urlpatterns + static(  # type: ignore
        # Serving media files in development only:
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
