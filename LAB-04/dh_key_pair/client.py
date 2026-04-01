import socket
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dh

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 65432))
    
    param_bytes = s.recv(4096)
    parameters = serialization.load_pem_parameters(param_bytes)
    s.sendall(b"ACK")
    
    server_pub_bytes = s.recv(4096)
    server_public_key = serialization.load_pem_public_key(server_pub_bytes)
    
    client_private_key = parameters.generate_private_key()
    client_public_key = client_private_key.public_key()
    
    client_pub_bytes = client_public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    s.sendall(client_pub_bytes)
    
    shared_key = client_private_key.exchange(server_public_key)
    print(f"Shared Secret (Client): {shared_key.hex()}")