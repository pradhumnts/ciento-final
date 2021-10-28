from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'affiliate/index.html')

def notifications(request):
    return render(request, 'affiliate/notifications.html')

def profile(request):
    return render(request, 'affiliate/profile.html')

def update_profile(request):
    return render(request, 'affiliate/update_profile.html')

def reset_password(request):
    return render(request, 'affiliate/reset_password.html')

def login(request):
    return render(request, 'affiliate/change_lang.html')
