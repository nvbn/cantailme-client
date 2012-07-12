import sys
import time
import json
import httplib
import os
import argparse
import webbrowser

class ServerProxy(object):
    def __init__(self, host):
        self.conn = httplib.HTTPConnection(host)

    def send(self, method, *args):
        data = json.dumps({
            'id': 'jsonrpc',
            'params': args,
            'method': method,
            'jsonrpc': '1.0'
        })
        self.conn.request('POST', '/json/', data, {})
        return json.loads(self.conn.getresponse().read())['result']


def main():
    parser = argparse.ArgumentParser(
        prog='tailme',
        description='Send tail session to remote service',
    )
    parser.add_argument('-s', '--silent', action='store_true', help='silent mode')
    parser.add_argument('-l', '--lines', type=int, default=5, help='lines per send')
    parser.add_argument('-r', '--remote', type=str, default='cantail.me', help='TailMe server')
    arg_result = parser.parse_args(sys.argv[1:])
    proxy = ServerProxy(arg_result.remote)
    data = proxy.send('create_session')
    hash = data['hash']
    secret = data['secret']
    if arg_result.silent:
        print 'Tail session page: http://%s/tail/%s/' % (arg_result.remote, hash)
    else:
        webbrowser.open('http://%s/tail/%s/' % (arg_result.remote, hash))
    to_send = []
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        if not arg_result.silent:
            sys.stdout.write(line)
        if line:
            to_send.append(line[:-1])
        if len(to_send) >= arg_result.lines:
            proxy.send('add_lines', hash, to_send)
            to_send = []
    if len(to_send):
        proxy.send('add_lines', hash, to_send)


if __name__ == '__main__':
    main()
