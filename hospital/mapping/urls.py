from django.urls import path
from . import views

urlpatterns = [
    path('', views.mapping_list_create, name='mapping_list_create'),  
    path('<int:id>/', views.mapping_delete, name='mapping_delete'),   
]
