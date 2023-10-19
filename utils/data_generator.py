import random
import string


def generate_string(length):
    letters_gen, numbers_gen = string.ascii_lowercase, string.digits
    letters = ''.join(random.choice(letters_gen) for i in range(length - 3))
    numbers = ''.join(random.choice(numbers_gen) for i in range(3))
    return letters + numbers


def generate_user_creds():
    return generate_string(10), generate_string(10)

