from django import forms
from app_general.models import Booking
from django.core.validators import RegexValidator

class BookingFrom(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["Seat","Room"]
class Fakecardform(forms.Form):
    exmonthchoice = [
        ("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),("6","6"),
        ("7","7"),("8","8"),("9","9"),("10","10"),("11","11"),("12","12")
    ]
    exyearchoice = [
        ("2023","2023"),("2024","2024"),("2025","2025"),("2026","2026"),
        ("2027","2027"),("2028","2028"),("2029","2029"),("2030","2030")
    ]
    numeric_validator = RegexValidator(
        regex=r'^[0-9]*$',
        message='Only numeric characters are allowed.',
    )
    alpha_validator = RegexValidator(
        regex=r'^[a-zA-Z]*$',
        message='Only alphabetic characters are allowed.',
    )

    Name = forms.CharField(max_length=50, validators=[alpha_validator])
    CreditCard = forms.CharField(max_length=16, validators=[numeric_validator])
    CVV = forms.CharField(max_length=3, validators=[numeric_validator])
    exmonth = forms.ChoiceField(choices=exmonthchoice,widget=forms.Select)
    exyear = forms.ChoiceField(choices=exyearchoice,widget=forms.Select)

    fields = ["Name","CreditCard","CVV","exyear","exmonth"]
