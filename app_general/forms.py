from django import forms
from app_general.models import Booking

class BookingFrom(forms.ModelForm):
    type = [
        ("card","Master/Visa/Credit cards"),
        ("credit","CreditPoint")
    ]
    Day = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    paymenttype = forms.ChoiceField(widget=forms.RadioSelect,choices=type)
    class Meta:
        model = Booking
        fields = ["Seat","Day","AccomName","Room","AirlineName","GuideName","paymenttype"]
class Fakecardform(forms.Form):
    exmonthchoice = [
        ("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),("6","6"),
        ("7","7"),("8","8"),("9","9"),("10","10"),("11","11"),("12","12")
    ]
    exyearchoice = [
        ("2023","2023"),("2024","2024"),("2025","2025"),("2026","2026"),
        ("2027","2027"),("2028","2028"),("2029","2029"),("2030","2030")
    ]
    Name = forms.CharField(max_length=50)
    CreditCard = forms.CharField(max_length=16)
    CVV = forms.CharField(max_length=3)
    exmonth = forms.ChoiceField(choices=exmonthchoice,widget=forms.Select)
    exyear = forms.ChoiceField(choices=exyearchoice,widget=forms.Select)

    fields = ["Name","CreditCard","CVV","exyear","exmonth"]
