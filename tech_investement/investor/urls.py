#urlpatterns

from django.urls import path
from . import views

urlpatterns = [
    path('adminDashboard', views.adminDashboard, name='adminDashboard'),
    path('', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('get_chart_data/', views.get_chart_data, name='get_chart_data'),
    ]

