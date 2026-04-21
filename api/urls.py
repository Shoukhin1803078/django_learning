from django.urls import path
from .views import BookListCreateAPIView, BookDetailAPIView

urlpatterns = [
    # /api/books/ - এখানে সব বই দেখা যাবে এবং নতুন বই তৈরি করা যাবে
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    
    # /api/books/1/ - এখানে নির্দিষ্ট বই (ID 1) দেখা, আপডেট ও ডিলিট করা যাবে
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
]