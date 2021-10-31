from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'administrator/index.html')

def add_administrator(request):
    return render(request, 'administrator/add_administrator.html')

def notifications(request):
    return render(request, 'administrator/notifications.html')

def profile(request):
    return render(request, 'administrator/profile.html')

def admin_member_profile(request):
    return render(request, 'administrator/admin_member_profile.html')

def admin_ambassador_profile(request):
    return render(request, 'administrator/admin_ambassador_profile.html')

def update_profile(request):
    return render(request, 'administrator/update_profile.html')

def reset_password(request):
    return render(request, 'administrator/reset_password.html')

def login(request):
    return render(request, 'administrator/change_lang.html')
