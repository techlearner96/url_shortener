import secrets
import string


def generate_short_code(length=6):
    if not isinstance(length, int) or isinstance(length, bool) or length <= 0:
        raise ValueError("Length must be a positive integer")
    characters = string.ascii_letters + string.digits

    return ''.join(
        secrets.choice(characters)
        for _ in range(length)
    )