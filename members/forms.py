from django import forms
from .models import User,Post
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email',]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data


    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")
        user.set_password(password)
        if commit:
            user.save()
        return user



class LoginForm(forms.Form):
    email = forms.CharField(
        max_length=100,
        widget=forms.EmailInput(attrs={'placeholder': "email"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': "password"})
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        user = authenticate(email=email,password=password)
        if user is None:
            raise ValidationError('невірний емаіл або пароль')
        self.user = user
        return cleaned_data


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFiledField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('widget', MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data,(list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result

class PostForm(forms.ModelForm):
    caption = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Напишіть щось...'})

    )
    images = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput()
    )
    class Meta:
        model = Post
        fields = ['images','caption']


