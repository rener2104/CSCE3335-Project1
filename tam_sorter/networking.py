# Networking functions for client and server
import socket
from .algorithm import SORT_TAM_SERVER


def start_server():
    HOST = '127.0.0.1'
    PORT = 9187
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print('Server listening on %s:%d...' % (HOST, PORT))
        print('Press Ctrl+C to exit')

        while True:
            conn, addr = s.accept()
            with conn:
                data = conn.recv(1024).decode().strip()
                if not data.endswith('#'):
                    response = "Input does not end with #"
                else:
                    datalist = list(data.strip('#'))
                    sorted_list = SORT_TAM_SERVER(datalist)
                    response = ''.join(sorted_list)
                conn.send(response.encode())


def start_client():
    HOST = '127.0.0.1'
    PORT = 9187
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        sequence = input("Enter sequence of 'T', 'A', 'M' letters ending with '#': ")

        s.send(sequence.encode())

        response = s.recv(1024).decode()
        print("Response from server: ", response)