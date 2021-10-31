from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'ambassador/index.html')

def add_ambassador(request):
    return render(request, 'ambassador/add_ambassador.html')

def membership(request):
    return render(request, 'ambassador/membership.html')

def invite_member(request):
    return render(request, 'ambassador/invite_member.html')

def invite_affiliate(request):
    return render(request, 'ambassador/invite_affiliate.html')

def notifications(request):
    return render(request, 'ambassador/notifications.html')

def profile(request):
    return render(request, 'ambassador/profile.html')

def update_profile(request):
    return render(request, 'ambassador/update_profile.html')

def reset_password(request):
    return render(request, 'ambassador/reset_password.html')

def login(request):
    return render(request, 'ambassador/change_lang.html')

def apply(request):
    return render(request, 'ambassador/change_lang.html')
