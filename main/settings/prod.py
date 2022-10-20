from .base import *

# on Live:

DEBUG = False
ALLOWED_HOSTS = [
    '127.0.0.1',
]

# LOGS:
LOGGING = { 
    "version": 1, 
    "disable_existing_loggers": True, 
    "formatters": { 
        'detail': { 
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}', 
            'style': '{', 
        },
    }, 
    "handlers": { 
        'file': { 
            'class': 'logging.FileHandler', 
            "formatter": "detail", 
            'filename': './prod_logs.log', 
            'level': 'INFO', 
        }, 
    }, 
    "loggers": { 
        "django": { 
            "handlers": ['file'], 
            "level": config("DJANGO_LOG_LEVEL", "INFO"), 
            'propagate': True, 
        }, 
    }, 
}


# SQLite:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'prod_db.sqlite3',
#     }
# }

# PostgreSQL:
DATABASES = { 
    "default": { 
        "ENGINE": "django.db.backends.postgresql_psycopg2", 
        "NAME": config("POSTGRESQL_DATABASE"), 
        "USER": config("POSTGRESQL_USER"), 
        "PASSWORD": config("POSTGRESQL_PASSWORD"), 
        "HOST": config("POSTGRESQL_HOST"), 
        "PORT": config("POSTGRESQL_PORT"), 
        "ATOMIC_REQUESTS": True, 
    }
}