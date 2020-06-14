#from django.shortcuts import render
import json
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.apps import apps

# Create your views here.
Users = apps.get_model('signup', 'Users')

class SigninView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            user_email = data['email']
            user_password = data['password']
            if Users.objects.filter(email=user_email):
                user_account = Users.objects.filter(email=user_email)[0]
                if user_account.password == user_password:
                    return HttpResponse(status=200)
                else:
                    return JsonResponse({'message':'INVALID_USER_CheckPW'}, status=401)
            else:
                return JsonResponse({'message':'INVALID_USER_CheckID'}, status=401)
        except Exception as e:
            return JsonResponse({'error_message':e})


    def get(self, request):
        user_data = Users.objects.values()
        return JsonResponse({'users':list(user_data)}, status=200)
