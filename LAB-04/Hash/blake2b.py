import hashlib

def hash_blake2b(data):
    h = hashlib.blake2b()
    h.update(data.encode('utf-8'))
    return h.hexdigest()

text = "BMTT Lab 04"
print(f"Blake2b: {hash_blake2b(text)}")