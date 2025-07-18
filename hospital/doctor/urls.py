from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                       # /api/doctor/
    path('<int:id>/', views.doctor_detail, name='detail'),   # /api/doctor/<id>/
]
