#urlpatterns

from django.urls import path
from . import views

urlpatterns = [
    #users
    path('user_profile/', views.user_profile, name='user_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('users/', views.users, name='users'),
    path('get_chart_data/', views.get_chart_data, name='get_chart_data'),
    
    #authentications
    path('', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('reset_confirm/', views.reset_confirm, name='reset_confirm'),
    path('reset_complete/', views.reset_complete, name='reset_complete'),
    path('reset_done/', views.reset_done, name='reset_done'),
    path('logout/', views.logout_view, name='logout'),
    
    #transactions
    path('transactions_history/', views.transactions_history, name='transactions_history'),
    path('transactions_pending/', views.transactions_pending, name='transactions_pending'),
    path('transactions_completed/', views.transactions_completed, name='transactions_completed'),
    path('deposit/', views.deposit, name='deposit'),
    path('withdraw/', views.withdraw, name='withdraw'),
    
    #assets
    path('assets/', views.assets, name='assets'),

    #admin
    path('admin_login/', views.adminLogin, name='admin_login'),
    path('adminDashboard', views.adminDashboard, name='adminDashboard'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('admin_login/', views.adminLogin, name='admin_login'),

    ]

