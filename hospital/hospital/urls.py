from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/doctor/', include('doctor.urls')),
    path('api/mapping/', include('mapping.urls')),
    path('api/patient/', include('patient.urls')),
    path('api/user/', include('authentication.urls')),
]
