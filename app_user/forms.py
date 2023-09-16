from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer
from django.core.validators import RegexValidator

numeric_validator = RegexValidator(
        regex=r'^[0-9]*$',
        message='Only numeric characters are allowed.',
    )
alpha_validator = RegexValidator(
    regex=r'^[ก-๏\s]*$',
    message='Only ตัวอักษรไทย are allowed.',
)
class RegisterForm(UserCreationForm):

    FirstName = forms.CharField(max_length = 25, validators=[alpha_validator])
    LastName = forms.CharField(max_length = 25, validators=[alpha_validator])
    Contract = forms.CharField(max_length = 10 ,validators=[numeric_validator])
    Email = forms.EmailField(max_length = 25)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'FirstName','LastName','Contract','Email')

class UserEditForm(forms.ModelForm):
    FirstName = forms.CharField(label='ชื่อจริง', widget=forms.TextInput, validators=[alpha_validator])
    LastName = forms.CharField(label='นามสกุล', widget=forms.TextInput, validators=[alpha_validator])
    Contract = forms.CharField(label='เบอร์โทรศัพท์', widget=forms.TextInput,validators=[numeric_validator])
    Email = forms.EmailField(label='อีเมล์', widget=forms.TextInput)

    class Meta:
        model = Customer
        fields = ("FirstName","LastName","Contract","Email")
