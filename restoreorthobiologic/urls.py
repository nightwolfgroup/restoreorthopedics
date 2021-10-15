""" restoreorthobiologic URL Configuration """
from django.contrib import admin
from django.urls import path, include
from wagtail.core import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.contrib.sitemaps.views import sitemap
from restoreorthobiologic import views

urlpatterns = [
    path('webmaster/', admin.site.urls),
    path('dashboard/', include(wagtailadmin_urls)),
    path('documentation/', include('documentation.urls')),
    path('sitemap.xml/', sitemap),
    path('', include(wagtail_urls)),
]

handler400 = views.bad_request
handler404 = views.page_not_found
handler403 = views.permission_denied
handler500 = views.server_error
