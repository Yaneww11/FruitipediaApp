from django.core.exceptions import ValidationError


class OnlyLettersValidator:
    def __init__(self, message="Fruit name should contain only letters!"):
        self.message = message

    def __call__(self, value: str):
        if not value.isalpha():
            return ValidationError(self.message)

    def deconstruct(self):
        return (
            'FruitipediaApp.fruits.validators.OnlyLettersValidator',
            (),
            {"message": self.message}
        )