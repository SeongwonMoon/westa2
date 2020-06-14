from django.shortcuts import render

# Create your views here.
import json
from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import Comments

class CommentView(View):
    def post(self, request):
        data = json.loads(request.body)
        Comments(
            name = data['name'],
            comment = data['comment'],
        ).save()
        return JsonResponse({'message':'SUCCESS'}, status=200)

    def get(self, request):
        comment_data = Comments.objects.values()
        return JsonResponse({'comments':list(comment_data)}, status=200)
