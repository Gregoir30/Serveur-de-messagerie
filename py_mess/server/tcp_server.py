import socket
import threading

#HOST = '127.0.0.1'
HOST = '192.168.0.155'
PORT = 5000
clients = []


def handle_client(conn, addr):
    print(f"[NOUVELLE CONNEXION] {addr} connecté.")
    while True:
        try:
            message = conn.recv(1024).decode('utf-8')
            if message:
                print(f"[{addr}] {message}")
                broadcast(message, conn)
        except ConnectionResetError:
            break
    conn.close()
    clients.remove(conn)
    print(f"[DÉCONNECTÉ] {addr} déconnecté.")


def broadcast(message, conn):
    for client in clients:
        if client != conn:
            client.send(message.encode('utf-8'))


def start_tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"[SERVEUR TCP] En écoute sur {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
