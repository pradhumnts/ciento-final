from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_up_otp', views.sign_up_otp, name='sign_up_otp'),
    path('membership/<str:membership_name>', views.membership, name='membership'),
    path('membership/<str:membership_name>/<str:affiliate_name>', views.affiliate, name='affiliate'),
    path('membership/<str:membership_name>/qr_code', views.qr_code, name='qr_code'),
    path('affiliate/<str:affiliate_name>/qr_scan', views.qr_scan, name='qr_scan'),
    path('notifications', views.notifications, name='notifications'),
    path('profile', views.profile, name='profile'),
    path('personal_info', views.personal_info, name='personal_info'),
    path('reset_password', views.reset_password, name='reset_password'),
    path('change_lang', views.change_lang, name='change_language')
]