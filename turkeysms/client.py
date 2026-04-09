import requests
import json

class TurkeySmsClient:
    """
    Official TurkeySMS API V4 Client for Python
    """
    BASE_URL = "https://api.turkeysms.com.tr/"

    def __init__(self, api_key):
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def _post(self, endpoint, data=None):
        if data is None:
            data = {}
        
        data['api_key'] = self.api_key
        url = f"{self.BASE_URL}{endpoint}"
        
        try:
            response = self.session.post(url, json=data, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {
                "status": "error",
                "result_code": "LOCAL-ERR",
                "result_message": str(e),
                "result": False
            }

    def send_sms(self, title, mobile, text, lang=0):
        """Send Standard SMS"""
        return self._post("sms/send", {
            "title": title,
            "mobile": mobile,
            "text": text,
            "sms_lang": lang
        })

    def send_otp(self, mobile, lang=2, digits=4):
        """Send OTP SMS"""
        return self._post("otp/send", {
            "mobile": mobile,
            "lang": lang,
            "digits": digits
        })

    def send_detailed_otp(self, title, mobile, text, lang=2):
        """Send Detailed OTP with custom text (Requires TS-CODE in text)"""
        return self._post("otp/detailed", {
            "title": title,
            "mobile": mobile,
            "text": text,
            "lang": lang
        })

    def get_balance(self):
        """Check Account Balance"""
        return self._post("balance/")

    def add_to_blacklist(self, number):
        """Add number to blacklist"""
        return self._post("blacklist/add", {"number": number})

    def get_sms_status(self, sms_id):
        """Check status of a sent SMS"""
        return self._post("sms/status", {"sms_id": sms_id})
