import socket

def start_client():
    host = '127.0.0.1'
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        message = input("Nhập tin nhắn gửi Server: ")
        s.sendall(message.encode())
        data = s.recv(1024)
        print(f"Phản hồi từ Server: {data.decode()}")

if __name__ == "__main__":
    start_client()