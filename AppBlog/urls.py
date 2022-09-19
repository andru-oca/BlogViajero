from django.urls import path, include

from AppBlog import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name="home"),
    path('about/', views.about, name="about"),
    # URLs de Posts
    path('posts/', views.PostListView.as_view(), name="posts"),
    path('detail-post/<int:pk>/', views.PostDetailView.as_view(), name="detail-post"),
    path('create-post/', views.PostCreateView.as_view(), name="create-post"),
    path('edit-post/<int:pk>/', views.PostUpdateView.as_view(), name="edit-post"),
    path('delete-post/<int:pk>/', views.PostDeleteView.as_view(), name="delete-post"),
    # URLS Perfil
    path('editar-perfil/', views.ProfileUpdateView.as_view(), name="editar_perfil"),
    path('agregar-avatar/', views.agregar_avatar, name="agregar_avatar"),
    # URLS Usuario y sesión
    path('login/', views.login_request, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('logout/', views.CustomLogoutView.as_view(), name = 'logout'),
]
