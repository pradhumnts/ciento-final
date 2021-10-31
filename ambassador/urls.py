from django.urls import path

from . import views

app_name = "ambassador"

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('apply', views.apply, name='apply'),
    path('membership', views.membership, name='membership'),
    path('profile', views.profile, name='profile'),
    path('notifications', views.notifications, name='notifications'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('add_ambassdor', views.add_ambassador, name='add_ambassador'),
    path('invite_member', views.invite_member, name='invite_member'),
    path('invite_affiliate', views.invite_affiliate, name='invite_affiliate'),
]