import os
import json
import psycopg2
from unipath import FSPath as Path


PROJECT_ENV = os.environ['PROJECT_ENV']
assert PROJECT_ENV in ['LOCAL', 'DEV', 'PROD']


# The full path to the repository root.
BASE = Path(__file__).absolute().ancestor(2)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '')


ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',

    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'rest_framework_swagger',
    'rules.apps.AutodiscoverRulesConfig',
    'django_extensions',
    'ckeditor',
    'ckeditor_uploader',

    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lambdaoj2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'lambdaoj2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['PGSQL_DB_NAME'],
        'HOST': os.environ['PGSQL_DB_HOST'],
        'PORT': int(os.environ['PGSQL_DB_PORT']),
        'USER': os.environ['PGSQL_DB_USER'],
        'PASSWORD': os.environ['PGSQL_DB_PASSWORD'],
        'CONN_MAX_AGE': int(os.environ['PGSQL_DB_CONN_MAX_AGE']),
        'OPTIONS': {
            'isolation_level': psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE,
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.environ['STATIC_ROOT']


# Media files

MEDIA_URL = '/media/'

MEDIA_ROOT = os.environ['MEDIA_ROOT']


# CKEditor

CKEDITOR_UPLOAD_PATH = 'ckeditor_uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'font_names': '宋体/宋体;黑体/黑体;仿宋/仿宋_GB2312;楷体/楷体_GB2312;隶书/隶书;幼圆/幼圆;微软雅黑/微软雅黑',
        'toolbar_Full': [
            {'name': 'document',
             'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard',
             'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing',
             'items': ['Find', 'Replace', '-', 'SelectAll', '-', 'Scayt']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select',
                       'Button', 'ImageButton', 'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript',
                       '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
                       'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter',
                       'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'Language']},
            {'name': 'links',
             'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley',
                       'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles',
             'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors',
             'items': ['TextColor', 'BGColor']},
            {'name': 'tools',
             'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about',
             'items': ['About']},
        ],
        'toolbar_Custom': [
            ['Bold', 'Italic', 'TextColor', 'BGColor'],
            ['Format', 'Font', 'FontSize'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
            ['Image', '-', 'Link', 'HorizontalRule', 'Table'],
            ['Undo', 'Redo'],
            ['Source', 'Preview'],
        ],
        'toolbar': 'Custom',
        'width': '100%',
        'tabSpaces': 4,
        # 'extraPlugins': 'image2',
        'extraPlugins': ','.join([
            'image2',
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
        ]),
        'enterMode': 3,  # 1: ENTER_P, 2: ENTER_BR, 3: ENTER_DIV
    },
}


# Auth

AUTH_USER_MODEL = 'main.User'

AUTHENTICATION_BACKENDS = [
    'rules.permissions.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
]

LOGIN_URL = 'rest_framework:login'
LOGOUT_URL = 'rest_framework:logout'


# Djoser

DJOSER = {
    'SET_PASSWORD_RETYPE': True,
    'LOGOUT_ON_PASSWORD_CHANGE': True,
}


# Django Rest Framework

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'lambdaoj2.pagination.CustomPageNumberPagination',
    'PAGE_SIZE': 10,
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ]
}


# Django Rest Swagger

SWAGGER_SETTINGS = {
    'DOC_EXPANSION': 'list',
}


# ENV specific settings

if PROJECT_ENV == 'LOCAL':
    DEBUG = True

elif PROJECT_ENV == 'DEV':
    DEBUG = True

elif PROJECT_ENV == 'PROD':
    DEBUG = False
