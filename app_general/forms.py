from django import forms
from app_general.models import Booking
from django.core.validators import RegexValidator

class BookingFrom(forms.ModelForm):
    seatchair = [
        ("A1","A1"),("B1","B1"),("C1","C1"),("D1","D1")
        ,("A2","A2"),("B2","B2"),("C2","C2"),("D2","D2")
        ,("A3","A3"),("B3","B3"),("C3","C3"),("D3","D3")
        ,("A4","A4"),("B4","B4"),("C4","C4"),("D4","D4")
        ,("A5","A5"),("B5","B5"),("C5","C5"),("D5","D5")
        ,("A6","A6"),("B6","B6"),("C6","C6"),("D6","D6")
        ,("A7","A7"),("B7","B7"),("C7","C7"),("D7","D7")
        ,("A8","A8"),("B8","B8"),("C8","C8"),("D8","D8")
        ,("A9","A9"),("B9","B9"),("C9","C9"),("D9","D9")
        ,("A10","A10"),("B10","B10"),("C10","C10"),("D10","D10")
    ]
    

    Seat = forms.MultipleChoiceField(choices=seatchair,widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Booking
        fields = ["Seat"]

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
        regex=r'^[a-z A-Z]*$',
        message='Only alphabetic characters are allowed.',
    )

    Name = forms.CharField(max_length=50, validators=[alpha_validator], widget=forms.TextInput(attrs={'id': 'name','style': 'width: 370px;'}),
        label='ชื่อเจ้าของบัตร'
        )
    CreditCard = forms.CharField(max_length=16, validators=[numeric_validator], widget=forms.TextInput(attrs={'id': 'card','style': 'width: 370px;'}),
        label='เลขบัตรเครดิต')
    CVV = forms.CharField(max_length=3, validators=[numeric_validator] , widget=forms.TextInput(attrs={'id': 'CVV','style': 'width: 45px;'}),
        label='เลข CVV')
    exmonth = forms.ChoiceField(choices=exmonthchoice,widget=forms.Select(attrs={'id': 'exmonth'}))
    exyear = forms.ChoiceField(choices=exyearchoice,widget=forms.Select(attrs={'id': 'exyear'}))

    fields = ["Name","CreditCard","CVV","exyear","exmonth"]