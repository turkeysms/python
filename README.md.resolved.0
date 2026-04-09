# TurkeySMS Python SDK (Official) 🐍

[![PyPI version](https://img.shields.io/pypi/v/turkeysms-python.svg)](https://pypi.org/project/turkeysms-python/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Official Python SDK for the **TurkeySMS API V4**. Seamlessly integrate SMS and OTP services into your Python applications.

## 🛠 Installation

Install the package via pip:

```bash
pip install turkeysms-python
```

---

## 🚀 Quick Start

### Initialize Client

```python
from turkeysms import TurkeySmsClient

client = TurkeySmsClient(api_key="your_api_key_here")
```

### Sending Standard SMS

```python
response = client.send_sms(
    title="SENDER",
    mobile="905xxxxxxxxx",
    text="Hello from TurkeySMS Python!",
    lang=0  # 0: English, 1: Turkish, 2: Arabic
)
print(response)
```

### Sending OTP SMS

Ultra-fast delivery for verification:

```python
response = client.send_otp(
    mobile="905xxxxxxxxx",
    lang=1,
    digits=4
)
```

### Advanced OTP (Custom Text)

```python
response = client.send_detailed_otp(
    title="SENDER",
    mobile="905xxxxxxxxx",
    text="Your security code is: TS-CODE",
    lang=1
)
```

### Check Balance

```python
balance = client.get_balance()
print(f"Current Balance: {balance.get('balance')}")
```

---

## 🛡 Security

If you discover any security-related issues, please email support@turkeysms.com.tr.

## 📄 License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.

---
© 2026 **TurkeySMS Bilişim ve İletيشim Hizmetleri Tic. Ltd. Şti.**
