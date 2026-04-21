from rest_framework import serializers
from blog.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # সব ফিল্ড নিবে
        