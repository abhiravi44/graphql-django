from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]

    username = models.CharField(
                                max_length=150, unique=True,
                                help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                                error_messages={"unique": "A user with that username already exists."},)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True, )


class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)

    def __str__(self):
        return self.name


