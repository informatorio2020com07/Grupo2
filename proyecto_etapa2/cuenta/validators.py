from django.core.exceptions import ValidationError

validar_num(value):
    if value.isdigit():
        return value
    else:
        raise ValidationError("son letras")
