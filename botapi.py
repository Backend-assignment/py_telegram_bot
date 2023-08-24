import requests

TOKEN = '5892121487:AAFJ8hXhSsCFBNMp-hHqFtAfwhO8RtCxdrM'
chat_id = 5575549228

button = {
    "text": 'button'
}

keyboard = [
    [button]
]

reply_markup = {
    "keyboard": keyboard
}

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

params = {
    "chat_id": chat_id,
    'text': 'hi',
    'reply_markup': reply_markup
}

response = requests.get(url, json=params)

print(response.json())