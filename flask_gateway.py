import requests
import json
from flask import Flask

api_url = 'https://api.jsonbin.io/b'
bin_ID = '5ce43b79838e9b0c10bcd344'
secret_key = '$2a$10$x6s7qqp.6PqaM5uyQoyIRu23f3awCM5freqJFM7Pfqdn3s5FgX7sa'


def read_from_db():
    url = f'{api_url}/{bin_ID}/latest'
    headers = {
        'secret-key': secret_key
    }
    req = requests.get(url, headers=headers)
    return req.json()


app = Flask(__name__)


@app.route('/new')
def novos_eps():
    db = read_from_db()

    text_list = []

    for show in db:
        for ep in show["newURLs"]:
            text_list.append(f'{show["tittle"]} - {ep["id"]}')

    if not text_list:
        return json.dumps({
            'speech': 'Desculpe, mas não há nada novo',
            'text': 'Não há novos episódios disponíveis'
        })

    else:
        return json.dumps({
            'speech': f'Aqui estão os {len(text_list)} novos episódios',
            'text': '\n'.join(text_list)
        })
