from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path('', views.index, name='index'),
    path('ambassador/login', views.login_ambassador, name='login-ambassador'),
    path('ambassador/register', views.register_ambassador, name='register-ambassador'),
    path('affiliate/login', views.login_affiliate, name='login-affiliate'),
    path('affiliate/register', views.register_affiliate, name='register-affiliate'),
    path('apply', views.apply_membership, name='apply'),
]