from datetime import datetime
from pprint import pprint
import time
import requests

URL = 'http://httpbin.org/post'

for i in range(3):
    response = requests.post(  # POST data to server
        URL,
        data={'date': datetime.now(),
            'label': 'test_' + str(i)
        },
        cookies={'python': 'testing'},
        headers={'X-Python': 'Guido van Rossum'},
    )
    if response.status_code in (requests.codes.OK, requests.codes.created):
        print(response.status_code)
        pprint(response.json())
        print()
        time.sleep(2)

