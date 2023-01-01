from django.core.validators import RegexValidator


class RegexValidations:
    only_letters_regex = RegexValidator(r'^[a-zA-Z\s]*$', 'Solo se admiten letras')
    only_numbers_regex = RegexValidator(r'^[0-9]*$', 'Solo se admiten números')
