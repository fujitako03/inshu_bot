from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello~~~~'

@app.route('/inshu')
def inshu_alert():
    import requests
    headers = {'Content-Type': 'application/json',}
    params = (('auth_token', 'ZBarJaGZsDrUNZbP9c7YDjRR6JCCF5eAw5e6fClJ'),)
    data = '{"color":"green","message":"@fujita","notify":false,"message_format":"text"}'
    response = requests.post('https://brainpad.hipchat.com/v2/room/1914775/notification', headers=headers, params=params, data=data)
    return 'inshu!'

if __name__ == '__main__':
    app.run()
