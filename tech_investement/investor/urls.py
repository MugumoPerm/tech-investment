#urlpatterns

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration_view, name='registration'),
    path('accounts/', views.login_view, name='login'),
    path('register/', views.register, name='register')
 
    ]

