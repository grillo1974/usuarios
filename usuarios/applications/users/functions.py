# Funciones extra de la aplicacion user

import random
import string
# genera un texto plano de 6 digitos
def code_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))