from django.urls import path, include

from AppBlog import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name="home"),
    path('about/', views.about, name="about"),
    # URLs Posts
    path('posts/', views.PostListView.as_view(), name="posts"),
    path('detail-post/<int:pk>/', views.PostDetailView.as_view(), name="detail-post"),
    path('create-post/', views.PostCreateView.as_view(), name="create-post"),
    path('edit-post/<int:pk>/', views.PostUpdateView.as_view(), name="edit-post"),
    path('delete-post/<int:pk>/', views.PostDeleteView.as_view(), name="delete-post"),
    # URLS Account
    path('account/edit/', views.ProfileUpdateView.as_view(), name="account_edit"),
    path('account/avatar-create/', views.AvatarCreateView.as_view(), name="account_avatar_create"),
    path('account/avatar-update/<int:pk>/', views.AvatarUpdateView.as_view(), name="account_avatar_update"),
    # URLS Login & Logout
    path('account/login/', views.CustomLoginView.as_view(), name = 'account_login'),
    path('account/register/', views.CustomRegisterView.as_view(), name = 'account_register'),
    path('account/logout/', views.CustomLogoutView.as_view(), name = 'account_logout'),
]
