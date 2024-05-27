from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class DrfpasswordlessConfig(AppConfig):
    name = 'auth-passwordless-kavenegar'
    verbose = _("auth Passwordless")