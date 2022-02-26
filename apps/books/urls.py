from django.urls import include, path
from . import views

urlpatterns = [
    path('slow/', views.BooksSlowEndpoint.as_view(), name="books_slow"),
    path('optimized/', views.BooksOptimizedEndpoint.as_view(), name="books_optimized")
]
