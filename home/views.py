from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse

# এটি আমাদের হোম পেজের ফাংশন
def home1(request):
    return HttpResponse("হ্যালো! এটি আমার প্রথম ডিজ্যাঙ্গো প্রোজেক্ট।")
    
def home2(request):
    return JsonResponse({
        "message": "Hello World"
    }
    )