from utils.sms import send_verify_pass_sms

def send_sms_with_callback_token(user, mobile_token, **kwargs):
    send_verify_pass_sms(user.mobile,mobile_token)
    return True