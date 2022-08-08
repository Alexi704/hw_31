from datetime import date
from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError

MIN_AGE = 9
FORBIDDEN_DOMAINS = [
    '@rambler',
    '@protonmail',
    '@startmail',
]


def check_age_validator(value: date):
    """Проверка, что пользователь старше 9 лет."""
    difference = relativedelta(date.today(), value).years
    if difference < MIN_AGE:
        raise ValidationError(
            "%(value) is too small.",
            params={"value", value}
        )


def check_email_validator(value):
    """Запрет на ввод почтового ящика из запрещенного списка."""
    for domain in FORBIDDEN_DOMAINS:
        if domain in value:
            raise ValidationError(
                "%(value) prohibited for registration in our service.",
                params={"value", value}
            )
