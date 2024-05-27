# Using auth-passwordless-kavenegar Package

## Installation
First, you need to add the following model to your user model:

```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None
    password = None
    mobile = models.CharField(
        max_length=13, 
        unique=True,
        db_index=True,
        help_text="Required. 13 characters mobile number",
        error_messages={
            "unique": ("A user with that mobile already exists."),
        },
        verbose_name='mobile'
    )

    USERNAME_FIELD = "mobile"

```

### Then add the following apps to your settings:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'drfpasswordless',
    'rest_framework_simplejwt',
    'auth-passwordless-kavenegar',
    ...
]
```

### Also, add the following configurations to your settings:

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
```

### And include the following URLs in your main urls.py:

```python

from django.urls import path, include

urlpatterns = [
    ...
    path('', include('auth-passwordless-kavenegar.urls')),
    ...
]

```

## Usage

### Endpoints
This package provides the following endpoints for authentication:

- `/auth/login/`: For user login request.
- `/auth/verify/`: For verifying the code sent to the user.
- `/auth/refresh/`: For token refreshing.

Note that if the user does not exist, they will be registered automatically, which can be adjusted from the settings.

### Installation
To use this package, first, make sure to add the following information to your Django project settings:

- `KAVENEGAR_API_KEY`: API key for Kavenegar SMS service.
- `KAVENEGAR_TEMPLATE`: Template ID for the SMS message.

Then, install the package using pip:

```bash
pip install auth-passwordless-kavenegar
