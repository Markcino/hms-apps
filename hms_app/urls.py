from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="dashboard"),
    path('add-staff', views.add_staff, name="add-staff"),
    path('site-config', views.site_config, name="site-config"),
    
]
