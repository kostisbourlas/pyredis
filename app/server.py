import socket

HOST = ""
PORT = 6379


def start_server():
    print(f"Initializing server in port {PORT}. . . ")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)
        conn, addr = s.accept()
        with conn:
            print(f"Connection accepted with addr {addr}")
            while True:
                data = conn.recv(2048)
                if not data:
                    break
                print("Message:", data)
