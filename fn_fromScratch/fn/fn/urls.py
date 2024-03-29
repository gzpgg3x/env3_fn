
from django.conf.urls import patterns, include, url
from django.contrib import admin

from mezzanine.core.views import direct_to_template


admin.autodiscover()


urlpatterns = patterns("",
    ("^admin/", include(admin.site.urls)),
    ("^", include("fn.main.urls")),
    ("^", include("mezzanine.urls")),
)

urlpatterns += patterns("",
    (r"^browserid/", include("django_browserid.urls")), # =persona
)

# Adds ``STATIC_URL`` to the context.
handler500 = "mezzanine.core.views.server_error"
