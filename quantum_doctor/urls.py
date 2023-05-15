from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quantum.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    # Other app urls...
]
