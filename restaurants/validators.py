from django.core.exceptions import ValidationError


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
        )


def validate_email(value):
    email = value
    if 'edu' in email:
        raise ValidationError('We do not accept edu emails')

CATEGORIES = ['Mexican', 'Asian', 'Fast Food', 'Misc']


def validate_category(value):
    cat = value.capitalize()    # allow non lower case entries
    if not value in CATEGORIES and not cat in CATEGORIES:
        raise ValidationError(f'{value} not a valid category')

