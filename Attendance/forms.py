import email

from django import forms

from Attendance.models import  Contact
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from Attendance.models import Contact
from django.contrib.auth.models import User


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "image": forms.ClearableFileInput(attrs = {'class': 'form-control', 'accept': 'images/*', 'title': 'Upload your image here'}),
            "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            "email": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            "age": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}),
            "position": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your position'}),
            "phoneNumber": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone'}),
        }


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

    def _str_(self):
        return f"{self.cleaned_data['username']} ({self.cleaned_data['password']})"

    def save(self):
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        return user


class AccountForm(UserCreationForm):
    email = forms.EmailField
    class Meta:
        model = User
        fields =['username','email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
}
