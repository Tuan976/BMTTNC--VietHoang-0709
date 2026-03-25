import hashlib

def hash_md5(data):
    md5_hash = hashlib.md5()
    md5_hash.update(data.encode('utf-8'))
    return md5_hash.hexdigest()

if __name__ == "__main__":
    text = input("Nhập chuỗi cần hash MD5: ")
    print(f"MD5: {hash_md5(text)}")