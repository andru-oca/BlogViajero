from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from datetime import date

from AppBlog.models import Profile, Post
from AppBlog.forms import  UserRegisterForm, UserUpdateForm, ProfileForm, PostForm


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 3
    ordering = ['id']

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')
        if query:
            return qs.filter(title__icontains=query)
        return qs

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


def about(request):
    return render(request, "about.html")

# Vistas de Posts
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'
    success_url = reverse_lazy('posts')


    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.date = date.today()
        return super(PostCreateView, self).form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'
    success_url = reverse_lazy('posts')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')


class ProfileCreateView(LoginRequiredMixin, CreateView):
    template_name = 'profile_create.html'
    success_url = reverse_lazy('home')
    form_class = ProfileForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProfileCreateView, self).form_valid(form)

# Views de Profile
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile_create.html'
    success_url = reverse_lazy('home')

# Views de account

class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('home')
    template_name = 'account_edit.html'

    def get_object(self, queryset=None):
        return self.request.user

class CustomLoginView(SuccessMessageMixin, LoginView):
    template_name = 'account_login.html'
    next_page = reverse_lazy('home')
    success_message = "You are successfully logged in"

class CustomRegisterView(SuccessMessageMixin, CreateView):
    template_name = 'account_register.html'
    success_url = reverse_lazy('home')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully. Please login to create & edit your favourite posts!"

class CustomLogoutView(LogoutView):
    template_name = 'account_logout.html'
    next_page = reverse_lazy('home')
