from django.urls import path

from . import views

app_name = "affiliate"
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('profile', views.profile, name='profile'),
    path('notifications', views.notifications, name='notifications'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('add_affiliate', views.add_affiliate, name='add_affiliate'),
]