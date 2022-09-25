from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppBlog.models import Profile, Post

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        def save(self, commit=True):
            user = super(UserRegisterForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image', 'name', 'webpage_link', 'description']

class PostForm(forms.ModelForm):

    class Meta:
        model = Post

        fields = ['title', 'subtitle', 'content', 'image']
        widgets = {
                'title': forms.TextInput(attrs={'class':'form-control'}),
                'subtitle':forms.TextInput(attrs={'class':'form-control'}),
                'content':forms.Textarea(attrs={'class':'form-control'}),
                }    