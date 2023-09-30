from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer
from django.core.validators import RegexValidator
from django.core.validators import MinLengthValidator, MaxLengthValidator

numeric_validator = RegexValidator(
        regex=r'^[0-9]*$',
        message='ต้องเป็นตัวเลขเท่านั้น',
    )
alpha_validator = RegexValidator(
    regex=r'^[ก-๏\s]*$',
    message='ต้องตัวอักษรไทยเท่านั้น',
)
class RegisterForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username','Class':'u-input u-input-rectangle u-block-c20c-29','id':'text-d11f'}))
    FirstName = forms.CharField(max_length = 25, validators=[alpha_validator],widget=forms.TextInput(
        attrs={'placeholder': 'Firstname','Class':'u-input u-input-rectangle u-block-c20c-40','id':'text-d78d'}))
    LastName = forms.CharField(max_length = 25, validators=[alpha_validator],widget=forms.TextInput(
        attrs={'placeholder': 'Lastname','Class':'u-input u-input-rectangle u-block-c20c-42','id':'text-5496'}))
    Contract = forms.CharField(max_length = 10 ,validators=[numeric_validator],widget=forms.TextInput(
        attrs={'placeholder': 'Contact','Class':'u-input u-input-rectangle u-block-c20c-45','id':'text-ce66'}))
    Email = forms.EmailField(max_length = 25,widget=forms.TextInput(
        attrs={'placeholder': 'Email address','Class':'u-input u-input-rectangle u-block-c20c-17','id':'email-5c33'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'u-input u-input-rectangle u-block-c20c-32', 'id': 'text-23c2'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password','Class':'u-input u-input-rectangle u-block-c20c-36','id':'text-5fac'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'FirstName','LastName','Contract','Email')

class UserEditForm(forms.ModelForm):
    CusFirstName = forms.CharField(label='ชื่อจริง', widget=forms.TextInput(attrs={'style': 'width: 140px; text-align: center; border: 1px solid rgba(0, 0, 0, 0.3);'}), validators=[alpha_validator],
                                   error_messages={'invalid': 'ชื่อ ต้องเป็นตัวอักษรไทยเท่านั้น'})
    CusLastName = forms.CharField(label='นามสกุล', widget=forms.TextInput(attrs={'style': 'width: 190px; text-align: center; border: 1px solid rgba(0, 0, 0, 0.3);'}), validators=[alpha_validator],
                                   error_messages={'invalid': 'นามสกุล ต้องเป็นตัวอักษรไทยเท่านั้น'})
    CusContract = forms.CharField(label='เบอร์โทรศัพท์',
            widget=forms.TextInput(attrs={'style': 'width: 230px; text-align: center; border: 1px solid rgba(0, 0, 0, 0.3);'}),
            validators=[
            numeric_validator,  # Your custom numeric validator
            MinLengthValidator(limit_value=7, message='เบอร์โทรศัพท์ต้องมีอย่างน้อย 7 ตัว'),
            MaxLengthValidator(limit_value=10, message='เบอร์โทรศัพท์ต้องมีไม่เกิน 10 ตัว')
        ],
        error_messages={'invalid': 'เบอร์โทรศัพท์ไม่ถูกต้อง'})
    CusEmail = forms.EmailField(label='อีเมล์', widget=forms.TextInput(attrs={'style': 'width: 475px; text-align: center; border: 1px solid rgba(0, 0, 0, 0.3);'}))

    class Meta:
        model = Customer
        fields = ("CusFirstName","CusLastName","CusContract","CusEmail")
