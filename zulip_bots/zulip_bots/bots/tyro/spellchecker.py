import sys
import os
sys.path.insert(0, os.getcwd())

import requests
import json
from typing import Dict, Any

Endpoint = "https://api.cognitive.microsoft.com/bing/v7.0/spellcheck"


# class spellcheckHandler(object):
#     def usage(self):
#         return '''
#             Enter some string we will check spelling mistakes for ya!
#         '''

def check_spellings(sentence)->str:
    apikey = "42b93138bab2469d9966a53fd4852a5b"
    print(sentence)
    mess = sentence

    data = {'text': sentence}

    params = {'mkt': 'en-us', 'mode': 'proof'}

    headers = {'Ocp-Apim-Subscription-Key': apikey,
               'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.post(Endpoint, headers=headers,
                             params=params, data=data)
    print(response.json())
    response = response.json()
    for ftokens in response['flaggedTokens']:
        wrong_word = ftokens['token']
        try:
            suggestion = ftokens['suggestions'][0]['suggestion']
            mess = mess.replace(wrong_word, suggestion, 1)
        except:
            mess = mess.replace(wrong_word, "<no word found>", 1)
    print(mess)
    return mess
# handler_class=spellcheckHandler
