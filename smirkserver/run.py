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

    route_info = server_lib.get_request_route_and_params(request_string)

    # Return index.html
    if route_info[0] == '/' and len(route_info[1]) < 1:
        return_resource = "index.html"

    # Return Route and parameters
    else:
        return_resource = route_info[0]

        if len(route_info[1]) > 0:
            parameters = server_lib.get_params_list(route_info[1])

            for p in parameters:
                line = 'name: {} value: {}\n'.format(p[0], p[1])


    response = "HTTP/1.1 200 OK\n\nROUTE:{}\nPARAMS:{}".format(return_resource, parameters).encode()
    connection.sendall(response)
    connection.close()
