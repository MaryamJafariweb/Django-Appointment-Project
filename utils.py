from kavenegar import *


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('2B673453366B314A4663377368546376393675694D4361623769524C5543636C4E6C54447A6F64784645553D')
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f'کد تایید شما {code} ',
        }
        response = api.sms_send(params)
        print(response)

    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
