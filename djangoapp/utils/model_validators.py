from django.core.exceptions import ValidationError

def validate_png(image):
    if not image.name.lower().endswith('.png'):
        print()
        print()
        print()
        print('Que chato')
        print()
        print()
        raise ValidationError('Imagem precisa ser PNG')