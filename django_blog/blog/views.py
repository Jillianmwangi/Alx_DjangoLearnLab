from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')

# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import CustomUserCreationForm

# Custom registration view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            return redirect('profile')  # Redirect to profile page after login
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

# User profile view (requires login)
@login_required
def profile(request):
    return render(request, 'blog/profile.html')

# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'blog/profile.html', context)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# ListView to display all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Specify the template to render
    context_object_name = 'posts'
    ordering = ['-published_date']  # Order by published_date descending

# DetailView to display a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# CreateView to allow users to create posts
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']  # Fields the user can fill

    def form_valid(self, form):
        form.instance.author = self.request.user  # Automatically set the author
        return super().form_valid(form)

# UpdateView to allow post authors to update their posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Ensure only the author can edit the post
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# DeleteView to allow authors to delete their posts
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')  # Redirect to post list after deletion

    # Ensure only the author can delete the post
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
