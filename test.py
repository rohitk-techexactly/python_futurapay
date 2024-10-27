from random import randint

# from Futurapay.Sdk.Gateway.Futurapay import FuturaPay

# from .Futurapay import FuturaPay
from Futurapay import FuturaPay

# Sample payload data
payment_payload = {
    "currency": "XAF",
    "amount": "50000",
    "customer_transaction_id": randint(10000000, 99999999),
    "country_code": "CM",
    "customer_first_name": "Tanmoy",
    "customer_last_name": "Sharma",
    "customer_phone": "8617821668",
    "customer_email": "rohitk.techexactly@gmail.com",
}

# Merchant details
merchant_key = "TMXXXXXXXXXXXXXXXX"
site_id = "831206409"
api_key = "apiKey66a33e22470a2"
env = "live"

# Create an instance of FuturaPay and initialize the payment
gateway = FuturaPay(merchant_key, api_key, site_id, env)
gateway.initialize(payment_payload)
