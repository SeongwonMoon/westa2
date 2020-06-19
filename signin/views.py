#from django.shortcuts import render
import json
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.apps import apps
import bcrypt
import jwt

# Create your views here.
from signup.models import Users

class SigninView(View):

    def post(self, request):
        data = json.loads(request.body)
        
        if set(data.keys()) != set(['email', 'password']):
            return JsonResponse({'Error':'Wrong Key Input, You Need eamil and password'}, status=400)

        try:
            user_email = data['email']
            user_pw = data['password']
            if Users.objects.filter(email=user_email):
                user_account = Users.objects.filter(email=user_email).values()[0]
                user_db_pw = user_account['password'].encode('utf-8')
                if bcrypt.checkpw(user_pw.encode('utf-8'), user_db_pw) == True:

                    #Token process
                    SECRET = 'secret'
                    id_target = user_account['id']
                    access_token = jwt.encode({'id' : id_target}, SECRET, algorithm = 'HS256')
                    return JsonResponse({'token': access_token.decode('utf-8')}, status=200)
                else:
                    return JsonResponse({'message':'INVALID_USER_CheckPW'}, status=401)
            else:
                return JsonResponse({'message':'INVALID_USER_CheckID'}, status=401)
        except Exception as e:
            return JsonResponse({'error_message':e})


    def get(self, request):
        user_data = Users.objects.values()
        return JsonResponse({'users':list(user_data)}, status=200)
