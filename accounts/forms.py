from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from phonenumber_field.formfields import PhoneNumberField

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "role"]

    # def clean_phone(self):
    #     phone = self.cleaned_data["phone"]
    #     if not phone.is_valid():
    #         raise ValidationError("Invalid phone number")
    #     return phone

    def is_valid(self):
        valid = super().is_valid()
        if not valid:
            return False
        return True
