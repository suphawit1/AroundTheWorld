from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    FirstName = forms.CharField(max_length = 25)
    LastName = forms.CharField(max_length = 25)
    Contract = forms.CharField(max_length = 10)
    Email = forms.EmailField(max_length = 25)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'FirstName','LastName','Contract','Email')