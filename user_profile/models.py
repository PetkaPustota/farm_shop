from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.validators import validate_international_phonenumber
from django.db import models
from authentication.models import AppUser


class ProfileUser(models.Model):
    user_id = models.OneToOneField(AppUser, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    address = models.TextField(null=True)

    phone = PhoneNumberField(region='RU', null=True)

    class Meta:
        ordering = ('first_name',)
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

