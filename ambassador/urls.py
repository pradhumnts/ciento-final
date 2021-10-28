from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('apply', views.apply, name='apply'),
    path('membership', views.membership, name='membership'),
    path('profile', views.profile, name='profile'),
    path('notifications', views.notifications, name='notifications'),
    path('update_profile', views.update_profile, name='update_profile'),
]