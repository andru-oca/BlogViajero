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
    # URLS Profile   
    path('account/profile-create/', views.ProfileCreateView.as_view(), name="profile_create"),
    path('account/profile-update/<int:pk>/', views.ProfileUpdateView.as_view(), name="profile_update"),
    # URLS Account
    path('account/login/', views.CustomLoginView.as_view(), name = 'account_login'),
    path('account/register/', views.CustomRegisterView.as_view(), name = 'account_register'),
    path('account/edit/', views.AccountUpdateView.as_view(), name="account_edit"),
    path('account/logout/', views.CustomLogoutView.as_view(), name = 'account_logout'),
]
