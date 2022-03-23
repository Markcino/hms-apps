# # from typing_extensions import Self
# from urllib import request
from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User


# Create your views here.

# class LoginView(View):
#     def get(self, request):
#         return render(request, 'authentication/login.html')
    
# #     def post(self, request):
#         username = request.POST['username']
#         password = request.POST['password']


class UsernameValidationView(View):
    def post(self, request):
        data=json.loads(request.body)
        username = data['username']

        if not str(username).isalnum():
            return JsonResponse({'username_eror':'username should be alphanumeric character'}, status=400)
        return JsonResponse({'username_valide': True})

        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_eror':'Sorry username in use, choose another'}, status=409)
        return JsonResponse({'username_valide': True})


class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')
