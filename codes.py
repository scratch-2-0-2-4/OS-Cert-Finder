import random
import string

def generer_code():
    ABC = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
    _123 = ''.join(random.choice(string.digits) for _ in range(3))
    def = ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
    return f"{ABC}-{_123}-{def}"

print(generer_code())
