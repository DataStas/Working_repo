# https://opentdb.com/api.php?amount=10&type=boolean
import requests

parametes = {
    'amount': 10,
    'type': 'boolean',
    'category': 18
}

response = requests.get(url='https://opentdb.com/api.php',
                        params=parametes)
response.raise_for_status()
data = response.json()['results']

question_data = data