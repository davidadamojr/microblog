import json

import requests
from flask_babel import _

from app import app


def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or not app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    auth = {
        'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY'],
        'Ocp-Apim-Subscription-Region': 'canadacentral'
    }
    response = requests.get(f'http://api.microsofttranslator.com/v2/Ajax.svc/Translate?'
                            f'text={text}&from={source_language}&to={dest_language}', headers=auth)
    if response.status_code != 200:
        return _('Error: the translation service failed.')
    return json.loads(response.content.decode('utf-8-sig'))