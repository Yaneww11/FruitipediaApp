from FruitipediaApp.fruits.validators import OnlyLettersValidator
from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(
        unique=True,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(2),
            OnlyLettersValidator(),
        ]
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    nutrition = models.TextField(
        null=True,
        blank=True,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.name
