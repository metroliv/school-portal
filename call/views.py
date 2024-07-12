from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def mute(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('userId')
        try:
            user = User.objects.get(user_id=user_id)
            user.muted = True
            user.save()
            return JsonResponse({'message': f'User {user_id} has been muted.'})
        except User.DoesNotExist:
            return JsonResponse({'message': 'User not found.'}, status=404)

@csrf_exempt
def unmute(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('userId')
        try:
            user = User.objects.get(user_id=user_id)
            user.muted = False
            user.save()
            return JsonResponse({'message': f'User {user_id} has been unmuted.'})
        except User.DoesNotExist:
            return JsonResponse({'message': 'User not found.'}, status=404)

@csrf_exempt
def remove(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('userId')
        try:
            user = User.objects.get(user_id=user_id)
            user.delete()
            return JsonResponse({'message': f'User {user_id} has been removed.'})
        except User.DoesNotExist:
            return JsonResponse({'message': 'User not found.'}, status=404)
