"""
Smirk - Web Application Framework
Copyright (c) 2016 Brett Fraley

Source Repository
https://github.com/bFraley/Smirk

MIT License
https://github.com/bFraley/Smirk/blob/master/LICENSE

File: smirkserver/run.py

About: Smirk's development server runtime
"""

import socket
import server_lib

smirk_host_instance = ''
smirk_port_instance = 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((smirk_host_instance, smirk_port_instance))
listen_socket.listen(1)
start_msg = '\nSmirk development server listening on port {}'.format(smirk_port_instance)
print(start_msg)

while True:
    connection, addr = listen_socket.accept()
    request = connection.recv(1024)
    request_string = bytes.decode(request)
    method = request_string.split(' ')[0]

    # Get Requested resource
    return_resource = ''

    url_file = request_string.split(' ')[1].split('?')[0]
    if url_file == '/':
        return_resource = "index.html"
    else:
        return_resource = url_file

    response = "HTTP/1.1 200 OK\n\n{}".format(return_resource).encode()
    connection.sendall(response)
    connection.close()
