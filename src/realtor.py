import os
import json
import requests


def notify():
    response = requests.get(os.environ['REALTOR_SEARCH_ENDPOINT'])
    results = json.loads(response.text)

    if results['searchCount'] != 0:
        event = os.environ['IFTTT_EVENT']
        key = os.environ['IFTTT_KEY']
        payload = {'value1': results['searchCount']}

        requests.post(
            f'https://maker.ifttt.com/trigger/{event}/with/key/{key}',
            data=payload,
        )
