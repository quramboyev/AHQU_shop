from django.core.exceptions import ValidationError

def validate_uzbek_phone(value):
    if not value.startswith('+998') or len(value) != 13 or not value[1:].isdigit():
        raise ValidationError('Введите корректный номер в формате +998XXXXXXXXX')
