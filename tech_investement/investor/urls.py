#urlpatterns

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #users
    path('', views.landing_page, name='landing_page'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('users/', views.users, name='users'),
    path('recommended_users/', views.recommended_users, name='recommended_users'),

    #authentications
    path('auth/login', views.login_view, name='login'),
    path('auth/reset_password/', auth_views.PasswordResetView.as_view(template_name='auth/reset_password.html'), name='reset_password'),
    path('auth/register/', views.register, name='register'),
    path('auth/register/<str:ref_code>/', views.register, name='register'),
    path('auth/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('auth/reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='reset_complete'),
    path('auth/reset_done/', auth_views.PasswordResetDoneView.as_view(), name='reset_done'),
    path('auth/logout/', views.logout_view, name='logout'),
    
    #transactions
    path('staff/admin/auth/transactions/', views.transactions, name='transactions'),
    path('transactions_history/', views.transactions_history, name='transactions_history'),
    path('transactions_pending/', views.transactions_pending, name='transactions_pending'),
    path('transactions_completed/', views.transactions_completed, name='transactions_completed'),
    path('deposit/', views.deposit, name='deposit'),
    path('withdraw/', views.withdraw, name='withdraw'),
    
    #assets
    path('assets/', views.assets, name='assets'),

    #admin
    path('staff/admin/auth/admin_login/', views.adminLogin, name='admin_login'),
    path('staff/admin/auth/adminDashboard', views.adminDashboard, name='adminDashboard'),
    path('staff/admin/auth/admin_workplace/', views.admin_workplace, name='admin_workplace'),
    path('staff/admin/auth/admin_logout/', views.admin_logout, name='admin_logout'),
    path('staff/admin/auth/admin_users/', views.admin_users, name='admin_users'),
    #charts(ajax)
    path('get_chart_data/', views.get_chart_data, name='get_chart_data'),

    ]

