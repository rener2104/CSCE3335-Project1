# Networking functions for client and server
import socket
from .algorithm import encode_integer  # Updated import

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
                while True:
                    data = conn.recv(1024).decode().strip()
                    if not data:
                        break  # Exit loop if connection is closed

                    try:
                        number = int(data)
                        if number < -121 or number > 121:
                            response = "Error: Number out of range (-121 to 121)"
                        else:
                            encoded = encode_integer(number)
                            response = str(encoded)
                    except ValueError:
                        response = "Error: Invalid integer input"

                    conn.send(response.encode())

def start_client():
    HOST = '127.0.0.1'
    PORT = 9187
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        while True:
            try:
                user_input = input("Enter an integer between -121 and 121: ").strip()

                s.send(user_input.encode())
                response = s.recv(1024).decode()
                print("Encoded response from server:")
                print(response)
            except KeyboardInterrupt:
                print("\nClient terminated.")
                break