from django.contrib import admin
from django.urls import include, path
from npa_api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('npa_api.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns) 