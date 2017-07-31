from settings import *
from game import *


game = Game()
players = {}


def web_server(env, start_response):
    if env["PATH_INFO"] == '/':
        r = (open('start.html').read() % (IP_ADDR, MAIN_PORT, WEB_PORT)).encode('utf-8')
    elif env["PATH_INFO"] == '/jquery.js':
        r = open('jquery.js').read().encode('utf-8')
    elif env["PATH_INFO"] == '/play':
        username = env['QUERY_STRING'].split('=')[1]
        role = game.getRole(username)
        if role == 's':
            r = (open('play_shooter.html').read() % (IP_ADDR, MAIN_PORT))
        elif role == 'p':
            r = (open('play_pilot.html').read() % (IP_ADDR, MAIN_PORT))
        else:
            r = "ERR_NOT_IN_GAME"
        r = r.encode('utf-8')
    else:
        r = b'ERR_INVALID_PATH'

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [r]


def process_request(data):
    print(data)
    if data['action'] == 'login':
        if data['username'] not in players:
            players[data['username']] = data['password']
        if players[data['username']] == data['password']:
            game.login(data['username'])
    elif data['action'] == 'attack':
        if players[data['username']] == data['password']:
            game.attack(data['username'])
    elif data['action'] == 'recharge':
        if players[data['username']] == data['password']:
            game.recharge(data['username'])


def action(env, start_response):
    if env["REQUEST_METHOD"] != "POST":
        start_response("403 Forbidden", [("Content-Type", "text/html; charset=utf-8")])
        return [b"ERR"]

    bytes = env["wsgi.input"].read()
    s = bytes.decode('utf-8')
    js = urllib.parse.unquote(s)[5:]
    data = json.loads(js)
    
    process_request(data)

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"ACC"]


if __name__ == '__main__':
    print('Starting server')
    threading.Thread(target = lambda : WSGIServer((IP_ADDR, MAIN_PORT), action) \
        .serve_forever(), args = ()).start()
    threading.Thread(target = lambda : WSGIServer((IP_ADDR, WEB_PORT), web_server) \
        .serve_forever(), args = ()).start()