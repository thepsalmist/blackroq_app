from .base import *

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "213.52.130.133", "www.blackroq.co.ke"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": "",
    }
}
