import json
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['ant.ieshm.org']

# Ruta del archivo secrets.json
BASE_DIR = Path(__file__).resolve().parent.parent
with open(BASE_DIR / 'settings' / 'secrets.json') as f:
    secrets = json.load(f)

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': secrets['DB_NAME'],
        'USER': secrets['DB_USER'],
        'PASSWORD': secrets['DB_PASSWORD'],
        'HOST': secrets['DB_HOST'],
        'PORT': secrets['DB_PORT'],
    }
}