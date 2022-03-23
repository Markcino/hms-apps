from django.shortcuts import render




def index(request):
    return render(request, 'hms/index.html')

def add_staff(request):
    return render(request, 'hms/add_staff.html')

def site_config(request):
    return render(request, 'hms/siteconfig.html')
