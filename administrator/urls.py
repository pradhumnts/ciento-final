from django.urls import path

from . import views

app_name = "administrator"

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('profile', views.profile, name='profile'),
    path('notifications', views.notifications, name='notifications'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('add_administrator', views.add_administrator, name='add_administrator'),
    path('admin_ambassador_profile', views.admin_ambassador_profile, name='admin_ambassador_profile'),
    path('admin_member_profile', views.admin_member_profile, name='admin_member_profile'),
]