<<<<<<< HEAD
from django.contrib.auth import authenticate
from blogapp.models import User
import random
from rest_framework.exceptions import AuthenticationFailed
from environs import Env

env = Env()
env.read_env()

def generate_username(name):
    username = name.lower()
    if not User.objects.filter(username=username).exists():
        return username
    else:
        random_username = username + str(random.randint(0, 1000))
        return generate_username(random_username)


def register_social_user(provider, user_id, email):
    name = email.split("@")[0]
    filtered_user_by_email = User.objects.filter(email=email)

    if filtered_user_by_email.exists():
        if provider == filtered_user_by_email[0].auth_provider:
            registered_user = authenticate(email=email, password=env("SOCIAL_SECRET"))

            return {
                "username": registered_user.username,
                "email": registered_user.email,
                "tokens": registered_user.tokens(),
            }

        else:
            raise AuthenticationFailed(
                detail="Please continue your login using "
                + filtered_user_by_email[0].auth_provider
            )

    else:
        user = {
            "username": generate_username(name),
            "email": email,
            "password": env("SOCIAL_SECRET"),
        }
        user = User.objects.create_user(**user)
        user.is_verified = True
        user.auth_provider = provider
        user.save()

        new_user = authenticate(email=email, password=env("SOCIAL_SECRET"))
        return {
            "email": new_user.email,
            "username": new_user.username,
            "tokens": new_user.tokens(),
        }
=======
from django.contrib.auth import authenticate
from blogapp.models import User
import random
from rest_framework.exceptions import AuthenticationFailed
from environs import Env

env = Env()
env.read_env()

def generate_username(name):
    username = name.lower()
    if not User.objects.filter(username=username).exists():
        return username
    else:
        random_username = username + str(random.randint(0, 1000))
        return generate_username(random_username)


def register_social_user(provider, user_id, email):
    name = email.split("@")[0]
    filtered_user_by_email = User.objects.filter(email=email)

    if filtered_user_by_email.exists():
        if provider == filtered_user_by_email[0].auth_provider:
            registered_user = authenticate(email=email, password=env("SOCIAL_SECRET"))

            return {
                "username": registered_user.username,
                "email": registered_user.email,
                "tokens": registered_user.tokens(),
            }

        else:
            raise AuthenticationFailed(
                detail="Please continue your login using "
                + filtered_user_by_email[0].auth_provider
            )

    else:
        user = {
            "username": generate_username(name),
            "email": email,
            "password": env("SOCIAL_SECRET"),
        }
        user = User.objects.create_user(**user)
        user.is_verified = True
        user.auth_provider = provider
        user.save()

        new_user = authenticate(email=email, password=env("SOCIAL_SECRET"))
        return {
            "email": new_user.email,
            "username": new_user.username,
            "tokens": new_user.tokens(),
        }
>>>>>>> dae3be574253c406cd0195a6ad252a205cc4b932
