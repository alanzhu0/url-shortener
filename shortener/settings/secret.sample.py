DEBUG = True
SECRET_KEY = "y_xy)s%b_0h=#=y#3le5wfk!iy_+w#3#2j_&g@k^u-^qbrhxl2"

AUTHENTICATION_BACKENDS = ("shortener.apps.auth.oauth.IonOauth2",)

if DEBUG:
    AUTH_PASSWORD_VALIDATORS = []
    AUTHENTICATION_BACKENDS += ("django.contrib.auth.backends.ModelBackend",)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "shortener",
        "USER": "shortener",
        "PASSWORD": "pwd",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

SENTRY_DSN = ""

CELERY_BROKER_URL = "redis://localhost/1"

SOCIAL_AUTH_REDIRECT_IS_HTTPS = False
SOCIAL_AUTH_ION_KEY = ""
SOCIAL_AUTH_ION_SECRET = ""
