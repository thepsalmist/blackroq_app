from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "message")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Name"}),
            "email": forms.EmailField(attrs={"placeeholder": "Email"}),
            "message": forms.Textarea(attrs={"placeholder": "Message..", "rows": 20}),
        }
