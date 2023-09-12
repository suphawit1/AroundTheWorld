from django import forms
from app_general.models import Booking
from app_user.models import Customer

class BookingFrom(forms.ModelForm):
    Day = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Booking
        fields = ["Seat","Day","AccomName","Room","AirlineName","GuideName"]