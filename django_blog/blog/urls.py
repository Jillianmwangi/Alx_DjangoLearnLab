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
