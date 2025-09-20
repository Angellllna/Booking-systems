from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ("check_in", "check_out", "comment")
        widgets = {
            "check_in":  forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "check_out": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "comment":   forms.Textarea(attrs={"rows": 3, "class": "form-control"}),
        }
