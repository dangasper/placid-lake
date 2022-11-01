from flask import Flask
from flask_talisman import Talisman

def init_app(app: Flask)
    SELF = "'self'"
    talisman = Talisman(
        app,
        content_security_policy={
            'default-src': SELF,
            'img-src': '*',
            'script-src': [
                SELF,
                'https://cdn.jsdelivr.net',
            ],
            'style-src': [
                SELF,
                'https://cdn.jsdelivr.net',
            ],
        },
        content_security_policy_nonce_in=['script-src'],
        feature_policy={
            'geolocation': '\'none\'',
        }
)   
