#urlpatterns

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #users
    path('user_profile/', views.user_profile, name='user_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('users/', views.users, name='users'),
    
    #authentications
    path('', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='reset_password.html'), name='reset_password'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='reset_complete'),
    path('reset_done/', auth_views.PasswordResetDoneView.as_view(), name='reset_done'),
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
    path('admin_workplace/', views.admin_workplace, name='admin_workplace'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('admin_users/', views.admin_users, name='admin_users'),
    #charts(ajax)
    path('get_chart_data/', views.get_chart_data, name='get_chart_data'),

    ]

