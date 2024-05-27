from kavenegar import KavenegarAPI,APIException,HTTPException
from kavenegar import *
from django.conf import settings

api_key = getattr(settings, 'KAVENEGAR_API_KEY', None)
template = getattr(settings, 'KAVENEGAR_TEMPLATE', None)

def send_verify_pass_sms(to_number, code,):
    if api_key:
        try:
            api = KavenegarAPI(settings.KAVENEGAR_API_KEY)
            params = {
                'receptor': to_number,
                'template': template,
                'token': code,
                'type': 'sms'
            }   
            response = api.verify_lookup(params)
            return True, response
        except APIException as e: 
            return False, str(e)
        except HTTPException as e: 
            return False, str(e)
    else:
        return False, "API key is not provided in settings"