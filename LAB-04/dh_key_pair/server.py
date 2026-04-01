import socket
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

parameters = dh.generate_parameters(generator=2, key_size=2048)
server_private_key = parameters.generate_private_key()
server_public_key = server_private_key.public_key()

param_bytes = parameters.parameter_bytes(serialization.Encoding.PEM, serialization.ParameterFormat.PKCS3)
server_pub_bytes = server_public_key.public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', 65432))
    s.listen(1)
    print("SERVER: Dang cho ket noi tai port 65432...")
    
    conn, addr = s.accept()
    with conn:
        print(f"SERVER: Da ket noi voi {addr}")
        conn.sendall(param_bytes)
        conn.recv(1024) 
        conn.sendall(server_pub_bytes)
        
        client_pub_bytes = conn.recv(2048)
        client_pub_key = serialization.load_pem_public_key(client_pub_bytes)
        
        shared_key = server_private_key.exchange(client_pub_key)
        print(f"SERVER Shared Secret: {shared_key.hex()[:32]}...")