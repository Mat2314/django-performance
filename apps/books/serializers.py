from rest_framework import serializers
from .models import Book
from apps.authors.serializers import AuthorSerializer


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=False, read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'price', 'author')
