from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # List all books
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet)

# The API URLs are determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Your other URL patterns
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
