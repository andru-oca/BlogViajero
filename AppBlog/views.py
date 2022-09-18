from typing import Dict

from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from AppBlog.models import Post
from AppBlog.forms import  UserRegisterForm, UserUpdateForm, AvatarFormulario


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")

# Vistas de Posts
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # form_class: PostForm
    fields = ['titulo', 'subtitulo', 'cuerpo']
    template_name = 'post_create.html'
    success_url = reverse_lazy('posts')

#fields = '__all__'

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['titulo', 'subtitulo']
    success_url = reverse_lazy('posts')


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts')


# Views de ususarios, registro, login o logout

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('home')
    template_name = 'perfil_edit.html'

    def get_object(self, queryset=None):
        return self.request.user


@login_required
def agregar_avatar(request):
    if request.method == 'POST':

        form = AvatarFormulario(request.POST, request.FILES) #aquí me llega toda la información del html

        if form.is_valid:   #Si pasó la validación de Django
            avatar = form.save()
            avatar.user = request.user
            avatar.save()
            return redirect(reverse('home'))

    form = AvatarFormulario() #Formulario vacio para construir el html
    return render(request, "perfil_avatar.html", {"form":form})


def register(request):
    mensaje = ''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "home.html", {"mensaje": "Usuario Creado :)"})
        else:
            mensaje = 'ADVERTENCIA: Cometiste un error en el registro !!!'

    formulario = UserRegisterForm()  # Formulario vacio para construir el html
    context = {
        'form': formulario,
        'mensaje': mensaje
    }

    return render(request, "perfil_register.html", context=context)

# Pass Administrador: BlogViajero2022
def login_request(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                return render(request, "home.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,"home.html", {"mensaje":"Error, datos incorrectos"})
        else:
            mensaje = "Los datos que intenta ingresar son incorrectos"
            formulario = AuthenticationForm()  # Formulario vacio para construir el html
            context = {
                'form': formulario,
                'mensaje': mensaje
            }
            return render(request,"perfil_login.html", context=context)

    form = AuthenticationForm()
    return render(request,"perfil_login.html", {'form':form} )


class CustomLogoutView(LogoutView):
    template_name = 'perfil_logout.html'
    next_page = reverse_lazy('home')
