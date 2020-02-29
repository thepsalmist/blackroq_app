from django import forms
from .models import Contact, Booking


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "message")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Name"}),
            "email": forms.TextInput(attrs={"placeeholder": "Email"}),
            "message": forms.Textarea(attrs={"placeholder": "Message..", "rows": 10}),
        }


class DateInput(forms.DateInput):
    input_type = "date"


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ("name", "email", "phone_number", "booking_date")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Name"}),
            "email": forms.TextInput(attrs={"placeholder": "Email"}),
            "phone_number": forms.NumberInput(),
            "booking_date": DateInput(),
        }

