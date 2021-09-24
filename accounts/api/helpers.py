from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


# function to get salt and hasher for creating hashed password
def generate_hashed_password(password):
    first_pass = User.objects.all()[0].password.split('$')
    hasher = first_pass[0]
    salt = first_pass[1]  # grabbing salt from the first password of the database

    return make_password(password, salt, hasher)