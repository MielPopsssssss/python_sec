import socket

def start_server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"[*] Attente de connexion sur {host}:{port}")
    client_socket, client_address = server_socket.accept()
    print(f"[*] Connexion établie avec {client_address}")

    while True:
        command = input("Shell> ")

        if command == 'QUIT':
            break

        client_socket.send(command.encode())
        result = client_socket.recv(1024).decode()
        print(result)

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
