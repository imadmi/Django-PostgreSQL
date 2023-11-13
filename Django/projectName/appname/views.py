from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse

def index(request):
    data = {'id': 1, 'name': 'John Doe'}
    return JsonResponse(data)