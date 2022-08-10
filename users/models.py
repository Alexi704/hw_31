from django.contrib.auth.models import AbstractUser
from django.db import models
from users.validators import check_age_validator, check_email_validator


class Location(models.Model):
    name = models.CharField(max_length=200, unique=True)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return self.name


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    ROLES = [
        (USER, USER),
        (MODERATOR, MODERATOR),
        (ADMIN, ADMIN),
    ]

    locations = models.ManyToManyField(Location, blank=True)
    role = models.CharField(max_length=9, choices=ROLES, default=USER)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    birth_date = models.DateField(validators=[check_age_validator], null=True)
    email = models.EmailField(unique=True, null=True, validators=[check_email_validator])

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        # ordering = ['username']

    def __str__(self):
        return self.username
