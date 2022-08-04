from datetime import datetime, timedelta
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.db import models


def check_birth_date(value: datetime):
    """Проверка, что пользователь старше 9 лет."""
    date_birthday = value.date()
    date_min_birthday = (datetime.today() - timedelta(days=365.25 * 9)).date()
    if date_birthday > date_min_birthday:
        raise ValidationError(f'Your age({date_birthday}) is too young.')


# def user_age(value: datetime):
#     """Вычисляем возраст пользователя"""
#     date_birthday = value.date()
#     date_today = datetime.today()
#     user_age_day = (date_today - date_birthday).days
#     user_age_year = int(user_age_day / 365.25)
#     return user_age_year


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
    # age = models.PositiveSmallIntegerField(null=True, blank=True)
    birth_date = models.DateTimeField(validators=[check_birth_date])
    # email = models.EmailField(unique=True, validators=[EmailValidator], null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        # ordering = ['username']

    def __str__(self):
        return self.username
