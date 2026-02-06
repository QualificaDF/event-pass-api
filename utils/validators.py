import re

def email_valido(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)
