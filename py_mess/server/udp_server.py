import socket

HOST = '127.0.0.1'
PORT = 5001
clients = set()


def start_udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((HOST, PORT))
    print(f"[SERVEUR UDP] En écoute sur {HOST}:{PORT}")

    while True:
        message, client_address = server_socket.recvfrom(1024)
        print(f"[{client_address}] {message.decode('utf-8')}")

        clients.add(client_address)
        for addr in clients:
            if addr != client_address:
                server_socket.sendto(message, addr)
