from django.conf import settings

PASSWORDLESS_AUTH = {
    'PASSWORDLESS_AUTH_TYPES': ['MOBILE'],
    'PASSWORDLESS_USER_MOBILE_FIELD_NAME': 'mobile',
    'PASSWORDLESS_REGISTER_NEW_USERS': True,
    'PASSWORDLESS_SMS_CALLBACK': 'utils.drfpasswordless.send_sms_with_callback_token',
    'PASSWORDLESS_AUTH_TOKEN_SERIALIZER': 'apps.users.serializers.CustomTokenSerializer',
    'PASSWORDLESS_TOKEN_EXPIRE_TIME': 2 * 60,
}

KAVENEGAR_API_KEY = getattr(settings, 'KAVENEGAR_API_KEY', None)
KAVENEGAR_TEMPLATE = getattr(settings, 'KAVENEGAR_TEMPLATE', None)