#from django.shortcuts import render
import json
from django.views import View
from django.http  import JsonResponse
from .models import Users
import bcrypt

#from django.core.exceptions import ValidationError
#from django.core.validators import validate_email

# Create your views here.
class MainView(View):
    def post(self, request):

        data = json.loads(request.body)
        if set(data.keys()) != set(['email', 'password']):
            return JsonResponse({'Error':'Wrong Key Input, You Need email and password'}, status=400)

        data['name'] = 'Mrs.Kim'
        pw_target = data['password']

        if Users.objects.filter(email=data['email']):
            return JsonResponse({'Error':'Already Email Exist'}, status=400)

        pw_target = data['password']
        hashed_password = bcrypt.hashpw(pw_target.encode('utf-8'), bcrypt.gensalt())
        decoded_pw = hashed_password.decode('utf-8')

        Users(
            name     = data['name'],
            email    = data['email'],
	    password = decoded_pw
            ).save()
        #print(Users.objects.all().values())
        return JsonResponse({'message':'SUCCESS'}, status=200)


    def get(self, request):
        user_data = Users.objects.values()
        return JsonResponse({'users':list(user_data)}, status=200)


