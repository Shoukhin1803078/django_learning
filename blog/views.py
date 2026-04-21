from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def blog_function(request):
    return HttpResponse("হ্যালো! এটি আমার প্রথম ব্লগ পেজ।")
