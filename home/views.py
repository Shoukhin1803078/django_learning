from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse

# এটি আমাদের হোম পেজের ফাংশন
def home1(request):
    return HttpResponse("Hello World ! This is my first Django project.")
    
def home2(request):
    return JsonResponse({
        "message": "Hello World"
    }
    )