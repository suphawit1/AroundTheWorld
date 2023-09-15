from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer

class RegisterForm(UserCreationForm):

    FirstName = forms.CharField(max_length = 25)
    LastName = forms.CharField(max_length = 25)
    Contract = forms.CharField(max_length = 10)
    Email = forms.EmailField(max_length = 25)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'FirstName','LastName','Contract','Email')

class UserEditForm(forms.ModelForm):
    class Meta:
        model = Customer
        FirstName = forms.CharField(label='ชื่อจริง', widget=forms.TextInput)
        LastName = forms.CharField(label='นามสกุล', widget=forms.TextInput)
        Contract = forms.CharField(label='เบอร์โทรศัพท์', widget=forms.TextInput)
        Email = forms.EmailField(label='อีเมล์', widget=forms.TextInput)

        fields = ("FirstName","LastName","Contract","Email")
