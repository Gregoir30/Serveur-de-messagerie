import socket

HOST = '192.168.0.151'
PORT = 56635


def start_udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("[CONNECTÉ] Vous pouvez envoyer des messages.")
    while True:
        message = input()
        client_socket.sendto(message.encode('utf-8'), (HOST, PORT))
