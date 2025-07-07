from random import SystemRandom
import string
from django.utils.text import slugify

def random_letter(k=5):
    return ''.join(SystemRandom().choices(
        string.ascii_letters + string.digits,
        k=k
    ))

def slugify_new(text, k = 5):
    return slugify(text) + '-' + random_letter(k)

print(slugify_new('Bla bla bla atenção'))