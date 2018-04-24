# from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from lodms.admin import admin_site
# import jet
from .views import home


urlpatterns =i18n_patterns(
    path('admin/', admin_site.urls),
        # path('admin/', testapp_admin_site.urls),
        path('', home),
        path('', include('casems.urls')),
        prefix_default_language=False,
        # path('', include('testapp.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += i18n_patterns(
#     path('^i18n/', include('django.conf.urls.i18n')),
# )
'''
if settings.DEBUG:
	from django.conf.urls import url
	import debug_toolbar
	urlpatterns = [
		url(r'^__debug__/', include(debug_toolbar.urls)),
	] + urlpatterns
'''
