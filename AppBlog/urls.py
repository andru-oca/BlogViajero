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
    path('account/edit/', views.ProfileUpdateView.as_view(), name="account_edit"),
    path('account/add-avatar/', views.AvatarRegisterView.as_view(), name="account_add_avatar"),
    # URLS Usuario y sesión
    path('account/login/', views.CustomLoginView.as_view(), name = 'account_login'),
    path('account/register/', views.CustomRegisterView.as_view(), name = 'account_register'),
    path('account/logout/', views.CustomLogoutView.as_view(), name = 'account_logout'),
]
