import requests
import hashlib

BASE_URL = "https://api.myltt.ltt.ly"
API_KEY = "UiFqpG0eZra3XfwzWFE7dNJP9B9ql6ZRA5kiSTBk"

DEVICE_MODEL = "unknown"
DEVICE_OS = "unknown"
OS_VERSION = "unknown"
USERNAME = "private"


def get_verification_code(phone_num: str, device_id: str) -> requests.Response:
    path = "/v1/mobile/verify"
    
    headers = {
        "X-API-KEY": API_KEY
    }

    data = {
        "mobile_number": phone_num,
        "device_unique_id": device_id
    }

    return requests.post(BASE_URL + path, headers=headers, data=data)


def verify_phone_num(otp: str, phone_num: str, device_id: str) -> requests.Response:
    path = "/v1/mobile/confirm"
    
    headers = {
        "X-API-KEY": API_KEY
    }

    data = {
        "verification_code": otp,
        "mobile_number": phone_num,
        "device_unique_id": device_id
    }

    return requests.post(BASE_URL + path, headers=headers, data=data)


def signup(phone_num: str, device_id: str) -> requests.Response:
    path = "/v1/signup"
    
    headers = {
        "X-API-KEY": API_KEY
    }

    data = {
        "mobile_number": phone_num,
        "device_unique_id": device_id,
        "device_model": DEVICE_MODEL,
        "device_os": DEVICE_OS,
        "device_os_version": OS_VERSION,
        "first_name": USERNAME,
        "last_name": USERNAME,
        "signup_type": 0
    }

    return requests.post(BASE_URL + path, headers=headers, data=data)


def get_token(client_id: str, client_secret: str, phone_num: str, device_id: str) -> requests.Response:
    path = "/oauth/token"
    
    headers = {
        "X-API-KEY": API_KEY
    }

    data = {
        "mobile_number": phone_num,
        "client_secret": client_secret,
        "client_id": client_id,
        "username": phone_num + "+" + device_id,
        "password": hashlib.sha512((device_id + "," + client_secret).encode()).hexdigest().upper(),
        "grant_type": "password"
    }

    return requests.post(BASE_URL + path, headers=headers, data=data)


def refresh_old_token(refresh_token: str, client_id: str, client_secret: str) -> requests.Response:
    path = "/oauth/token"
    
    headers = {
        "X-API-KEY": API_KEY
    }

    data = {
        "client_secret": client_secret,
        "client_id": client_id,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token"
    }

    return requests.post(BASE_URL + path, headers=headers, data=data)


def validate_token(token: str) -> requests.Response:
    path = "/v1/validate-token"
    
    headers = {
        "X-API-KEY": API_KEY,
        "Authorization": "Bearer " + token
    }

    return requests.get(BASE_URL + path, headers=headers)


def delete_account(token: str) -> requests.Response:
    path = "/v1/account"
    
    headers = {
        "X-API-KEY": API_KEY,
        "Authorization": "Bearer " + token
    }

    return requests.delete(BASE_URL + path, headers=headers)


def get_services() -> requests.Response:
    path = "/v1/services"
    
    headers = {
        "X-API-KEY": API_KEY
    }

    return requests.get(BASE_URL + path, headers=headers)


def get_service_info(service_type_id: str) -> requests.Response:
    path = "/v1/services/" + service_type_id 
    
    headers = {
        "X-API-KEY": API_KEY
    }

    return requests.get(BASE_URL + path, headers=headers)


def add_service(service_type_id: str, friendly_name: str, service_credentials: dict, token: str) -> requests.Response:
    path = "/v1/account/services"

    headers = {
        "X-API-KEY": API_KEY,
        "Authorization": "Bearer " + token
    }

    data = service_credentials.copy()
    data["service_type"] = service_type_id
    data["friendly_name"] = friendly_name

    return requests.post(BASE_URL + path, headers=headers, data=data)


def update_friendly_name(friendly_name: str, service_id: str, token: str) -> requests.Response:
    path = "/v1/account/services/" + service_id + "/update-friendly-name"
    
    headers = {
        "X-API-KEY": API_KEY,
        "Authorization": "Bearer " + token
    }
    
    data = {
        "friendly_name": friendly_name
    }

    return requests.post(BASE_URL + path, headers=headers, data=data)


def get_user_service_info(service_credentials: dict, service_id: str, token: str) -> requests.Response:
    path = "/v1/account/services/" + service_id

    headers = {
        "X-API-KEY": API_KEY,
        "Authorization": "Bearer " + token
    }

    data = service_credentials.copy()

    return requests.post(BASE_URL + path, headers=headers, data=data)


def delete_service(service_id: str, token: str) -> requests.Response:
    path = "/v1/account/services/" + service_id
    
    headers = {
        "X-API-KEY": API_KEY,
        "Authorization": "Bearer " + token
    }

    return requests.delete(BASE_URL + path, headers=headers)


def get_auto_recharge_status(service_id: str, token: str) -> requests.Response:
    path = "/v1/account/services/" + service_id + "/auto-recharge"
    
    headers = {
        "X-API-KEY": API_KEY,
        "Authorization": "Bearer " + token
    }

    return requests.get(BASE_URL + path, headers=headers)


def toggle_auto_recharge_status(service_id: str, token: str) -> requests.Response:
    path = "/v1/account/services/" + service_id + "/auto-recharge"
    
    headers = {
        "X-API-KEY": API_KEY,
        "Authorization": "Bearer " + token
    }
    
    data = {
        "status": 1
    }

    return requests.post(BASE_URL + path, headers=headers, data=data)


def recharge_voucher(voucher: str, service_credentials: dict, service_id: str, token: str) -> requests.Response:
    path = "/v1/account/services/" + service_id + "/top-up"
    
    headers = {
        "X-API-KEY": API_KEY,
        "Authorization": "Bearer " + token
    }

    data = service_credentials.copy()
    data["voucher"] = voucher

    return requests.post(BASE_URL + path, headers=headers, data=data)


def get_package_categories() -> requests.Response:
    path = "/v1/products"
    
    headers = {
        "X-API-KEY": API_KEY
    }

    return requests.get(BASE_URL + path, headers=headers)


def get_packages(category_id: str) -> requests.Response:
    path = "/v1/products/" + category_id
    
    headers = {
        "X-API-KEY": API_KEY
    }

    return requests.get(BASE_URL + path, headers=headers)


def subscribe_to_package(package_id: str, service_credentials: dict, service_id: str, token: str) -> requests.Response:
    path = "/v1/account/services/" + service_id + "/package"

    headers = {
        "X-API-KEY": API_KEY,
        "Authorization": "Bearer " + token
    }

    data = service_credentials.copy()
    data["package_id"] = package_id

    return requests.post(BASE_URL + path, headers=headers, data=data)
