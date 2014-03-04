DEBUG = True
SANDBOX = True
TEMPLATE_DEBUG = DEBUG

DEBUG = True
SANDBOX = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'angular_todo_app',
        'USER': '',
        'PASSWORD': '',
        'HOST': ''
    }
}

ALLOWED_HOSTS = ['localhost']