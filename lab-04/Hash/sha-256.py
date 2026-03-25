import hashlib

def hash_sha256(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    return sha256_hash.hexdigest()

text = "BMTT Lab 04"
print(f"SHA-256: {hash_sha256(text)}")