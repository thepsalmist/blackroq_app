from .base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "blackroq.herokuapp.com", "www.blackroq.co.ke"]


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
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES["default"].update(db_from_env)

