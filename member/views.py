from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'member/index.html')

def membership(request, membership_name):
    return render(request, 'member/membership/membership.html')

def affiliate(request, affiliate_name):
    return render(request, 'member/membership/affiliate.html')

def qr_code(request, membership_name):
    return render(request, 'member/membership/qr_code.html')

def qr_scan(request, affiliate_name):
    return render(request, 'member/affiliate/qr_scan.html')

def notifications(request):
    return render(request, 'member/notifications.html')

def profile(request):
    return render(request, 'member/profile.html')

def personal_info(request):
    return render(request, 'member/personal_info.html')

def reset_password(request):
    return render(request, 'member/reset_password.html')

def change_lang(request):
    return render(request, 'member/change_lang.html')

def login(request):
    return render(request, 'member/change_lang.html')

def sign_up(request):
    return render(request, 'member/change_lang.html')

def sign_up_otp(request):
    return render(request, 'member/change_lang.html')
