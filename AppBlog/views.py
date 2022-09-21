from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from datetime import date

from AppBlog.models import Post
from AppBlog.forms import  UserRegisterForm, UserUpdateForm, AvatarFormulario, PostForm


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 3

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


# Views de ususarios, registro, login o logout

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('home')
    template_name = 'perfil_edit.html'

    def get_object(self, queryset=None):
        return self.request.user


class AvatarRegisterView(LoginRequiredMixin, CreateView):
    template_name = 'perfil_avatar.html'
    success_url = reverse_lazy('home')
    form_class = AvatarFormulario

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AvatarRegisterView, self).form_valid(form)

# Pass Administrador: BlogViajero2022

class CustomLoginView(LoginView):
    template_name = 'perfil_login.html'
    next_page = reverse_lazy('home')

class CustomRegisterView(SuccessMessageMixin, CreateView):
    template_name = 'perfil_register.html'
    success_url = reverse_lazy('home')
    form_class = UserRegisterForm
    # success_message = "Your profile was created successfully"

class CustomLogoutView(LogoutView):
    template_name = 'perfil_logout.html'
    next_page = reverse_lazy('home')
