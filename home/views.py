from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# এটি আমাদের হোম পেজের ফাংশন
def home_function(request):
    return HttpResponse("হ্যালো! এটি আমার প্রথম ডিজ্যাঙ্গো প্রোজেক্ট।")