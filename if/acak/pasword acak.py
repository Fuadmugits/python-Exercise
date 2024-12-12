import random
import string

def buat_password(panjang=12):
    karakter = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(karakter) for i in range(panjang))
    return password

print("Password acak:", buat_password())