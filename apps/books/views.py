from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Book
from .serializers import BookSerializer


# Create your views here.
class BooksSlowEndpoint(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        """In here there are too many database queries being done and slowing down the server response"""
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)
        return Response(serializer.data)


class BooksOptimizedEndpoint(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        all_books = Book.objects.all().prefetch_related("author")
        serializer = BookSerializer(all_books, many=True)

        return Response(serializer.data)
