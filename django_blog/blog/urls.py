# blog/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]

# blog/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Login URL (Django's built-in LoginView)
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),

    # Logout URL (Django's built-in LogoutView)
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Custom Registration View
    path('register/', views.register, name='register'),

    # User Profile View (requires login)
    path('profile/', views.profile, name='profile'),
]

# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
]

from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('new/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    # URL pattern for listing all posts
    path('', PostListView.as_view(), name='post-list'),
    
    # URL pattern for viewing details of a single post
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    
    # URL pattern for creating a new post
    path('new/', PostCreateView.as_view(), name='post-create'),
    
    # URL pattern for editing an existing post
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),
    
    # URL pattern for deleting an existing post
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
