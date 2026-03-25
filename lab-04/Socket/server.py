import socket

def start_server():
    host = '127.0.0.1'
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server đang chạy tại {host}:{port}...")
        
        conn, addr = s.accept()
        with conn:
            print(f"Đã kết nối bởi {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Nhận từ Client: {data.decode()}")
                conn.sendall(b"Server da nhan duoc tin nhan!")

if __name__ == "__main__":
    start_server()