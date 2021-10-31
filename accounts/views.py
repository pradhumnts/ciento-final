from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')

def login_ambassador(request):
    return render(request, 'accounts/login-ambassador.html')

def register_ambassador(request):
    return render(request, 'accounts/index.html')

def login_affiliate(request):
    return render(request, 'accounts/login-affiliate.html')

def register_affiliate(request):
    return render(request, 'accounts/index.html')

def apply_membership(request):
    return render(request, 'accounts/apply.html')
