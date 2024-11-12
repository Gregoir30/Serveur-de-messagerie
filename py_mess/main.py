def start():
    mode = input("Voulez-vous démarrer en tant que serveur (s) ou client (c) ? ").strip().lower()
    protocol = input("Choisissez le protocole : TCP (t) ou UDP (u) ? ").strip().lower()

    if mode == 's':
        if protocol == 't':
            from server.tcp_server import start_tcp_server
            start_tcp_server()
        elif protocol == 'u':
            from server.udp_server import start_udp_server
            start_udp_server()
    elif mode == 'c':
        if protocol == 't':
            from client.tcp_client import start_tcp_client
            start_tcp_client()
        elif protocol == 'u':
            from client.udp_client import start_udp_client
            start_udp_client()


if __name__ == "__main__":
    start()
