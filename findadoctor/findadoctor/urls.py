from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('accounts.urls')),
    path('', include('finderapp.urls')),
    path('admin/', admin.site.urls),
]
