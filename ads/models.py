from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(5)])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=200, validators=[MinLengthValidator(10)])
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    description = models.TextField(max_length=2000, blank=True)
    is_published = models.BooleanField(default=False, blank=True)
    image = models.ImageField(upload_to='logos/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=200, unique=True)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name
