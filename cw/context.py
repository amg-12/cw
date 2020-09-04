import random

LAST = 251


def num(request):
    return {'mon': f'{random.randint(1, LAST):03}', 'last': LAST}
