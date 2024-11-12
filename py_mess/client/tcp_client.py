import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

def receive_messages(conn):
    while True:
        try:
            message = conn.recv(1024).decode('utf-8')
            if message:
                print(f"[Message reçu] {message}")
        except ConnectionResetError:
            break

def start_tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    print("[CONNECTÉ] Vous pouvez envoyer des messages.")
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))
