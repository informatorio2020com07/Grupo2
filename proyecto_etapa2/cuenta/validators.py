from django.core.exceptions import ValidationError

def validar_num(value):
    if value.isdigit():
        return value
    else:
        raise ValidationError("son letras")
