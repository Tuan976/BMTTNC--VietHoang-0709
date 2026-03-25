from md5_library import hash_md5

def main():
    message = "Hello Viet Hoang"
    result = hash_md5(message)
    print(f"Message: {message}")
    print(f"Hash Result: {result}")

if __name__ == "__main__":
    main()