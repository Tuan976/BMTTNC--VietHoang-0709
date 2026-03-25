import hashlib

def hash_sha3_256(data):
    # SHA-3 có sẵn trong hashlib từ Python 3.6+
    sha3 = hashlib.sha3_256()
    sha3.update(data.encode('utf-8'))
    return sha3.hexdigest()

text = "BMTT Lab 04"
print(f"SHA-3 (256): {hash_sha3_256(text)}")