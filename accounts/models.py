from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django import forms
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    # User = get_user_model()
    # phone = PhoneNumberField(blank=True, queryset=User.objects.all())

    class Role(models.TextChoices):
        ADMIN = "AM", "Admin"
        AUTHOR = "AT", "Author"
        EDITOR = "ET", "Editor"

    role = models.CharField(
        "User Role", max_length=2, default=Role.AUTHOR, choices=Role.choices
    )
    def __str__(self):
        return self.username
