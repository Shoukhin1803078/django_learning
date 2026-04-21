from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.shortcuts import get_object_or_404
from blog.models import Book
from .serializers import BookSerializer

# 1. সব বই দেখা (GET) এবং নতুন বই তৈরি (POST)
class BookListCreateAPIView(APIView):
    
    # GET: সব বইয়ের তালিকা দেখাবে
    def get(self, request):
        books = Book.objects.all()  # সব বই ডাটাবেস থেকে আনলাম
        serializer = BookSerializer(books, many=True)  # অনেকগুলো object কে JSON এ কনভার্ট
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # POST: নতুন বই তৈরি করবে
    def post(self, request):
        serializer = BookSerializer(data=request.data) # ইউজারের পাঠানো ডাটা নিলাম
        if serializer.is_valid():  # ডাটা ঠিক আছে কিনা চেক
            serializer.save()  # ডাটাবেসে সেভ করলাম
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 2. নির্দিষ্ট একটি বই দেখা (GET), আপডেট (PUT/PATCH) এবং ডিলিট (DELETE)
class BookDetailAPIView(APIView):
    
    # helper method: বইটি খুঁজে বের করা (পুনরায় ব্যবহারের জন্য)
    def get_object(self, pk):
        return get_object_or_404(Book, pk=pk)
    
    # GET: নির্দিষ্ট একটি বই দেখা
    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # PUT: সম্পূর্ণ বই আপডেট করা
    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # PATCH: আংশিক আপডেট করা (শুধু যে ফিল্ডগুলো পাঠাবে সেগুলো আপডেট করবে)
    def patch(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data, partial=True)  # partial=True মানে আংশিক আপডেট
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE: বই ডিলিট করা
    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response({'message': 'বইটি ডিলিট করা হয়েছে'}, status=status.HTTP_204_NO_CONTENT)