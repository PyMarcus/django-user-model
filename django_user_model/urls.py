from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('padm/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('users.urls'))
]


# personalize admin site

admin.site.site_header = 'ADM'
admin.site.site_title = 'MDA'
admin.site.index_title = 'System'
