from django.contrib import admin
from django.urls import path
from app_geoip import views

urlpatterns = [
    # Rota url, view responsável, nome de referência
    # path('admin/', admin.site.urls),
    path('', views.home2, name='home'),
    #path('dashboard/', views.dashboard, nome='dashboard')

]
