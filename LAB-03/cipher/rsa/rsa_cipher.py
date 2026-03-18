import rsa, os, sys
from PyQt5 import QtWidgets

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from ui.rsa import Ui_Dialog

if not os.path.exists('cipher/rsa/keys'):
    os.makedirs('cipher/rsa/keys')

class RSACipher:
    def __init__(self):
        pass

    def generate_keys(self):
        (public_key, private_key) = rsa.newkeys(1024)
        with open('cipher/rsa/keys/publicKey.pem', 'wb') as p:
            p.write(public_key.save_pkcs1('PEM'))
        with open('cipher/rsa/keys/privateKey.pem', 'wb') as p:
            p.write(private_key.save_pkcs1('PEM'))

    def load_keys(self):
        with open('cipher/rsa/keys/publicKey.pem', 'rb') as p:
            public_key = rsa.PublicKey.load_pkcs1(p.read())
        with open('cipher/rsa/keys/privateKey.pem', 'rb') as p:
            private_key = rsa.PrivateKey.load_pkcs1(p.read())
        return private_key, public_key

    def encrypt(self, message, key):
        return rsa.encrypt(message.encode('utf-8'), key)

    def decrypt(self, ciphertext, key):
        try:
            return rsa.decrypt(ciphertext, key).decode('utf-8')
        except:
            return False

    def sign(self, message, key):
        return rsa.sign(message.encode('utf-8'), key, 'SHA-1')

    def verify(self, message, signature, key):
        try:
            return rsa.verify(message.encode('utf-8'), signature, key) == 'SHA-1'
        except:
            return False

class MainApp(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.rsa_cipher = RSACipher()
        self.rsa_cipher.generate_keys()
        
        self.ui.pushButton.clicked.connect(self.handle_encrypt)
        self.ui.pushButton_2.clicked.connect(self.handle_decrypt)
        self.ui.pushButton_3.clicked.connect(self.handle_sign)
        self.ui.pushButton_4.clicked.connect(self.handle_verify)

    def handle_encrypt(self):
        message = self.ui.txt_plaintext.toPlainText()
        if message:
            _, public_key = self.rsa_cipher.load_keys()
            encrypted = self.rsa_cipher.encrypt(message, public_key)
            self.ui.txt_CurrentText.setPlainText(encrypted.hex())

    def handle_decrypt(self):
        hex_text = self.ui.txt_CurrentText.toPlainText()
        if hex_text:
            private_key, _ = self.rsa_cipher.load_keys()
            ciphertext = bytes.fromhex(hex_text)
            decrypted = self.rsa_cipher.decrypt(ciphertext, private_key)
            if decrypted:
                self.ui.txt_plaintext.setPlainText(decrypted)
            else:
                QtWidgets.QMessageBox.critical(self, "Lỗi", "Giải mã thất bại!")

    def handle_sign(self):
        message = self.ui.txt_Information.toPlainText()
        if message:
            private_key, _ = self.rsa_cipher.load_keys()
            signature = self.rsa_cipher.sign(message, private_key)
            self.ui.txt_Siganture.setPlainText(signature.hex())

    def handle_verify(self):
        message = self.ui.txt_Information.toPlainText()
        sig_hex = self.ui.txt_Siganture.toPlainText()
        if message and sig_hex:
            _, public_key = self.rsa_cipher.load_keys()
            try:
                signature = bytes.fromhex(sig_hex)
                is_valid = self.rsa_cipher.verify(message, signature, public_key)
                if is_valid:
                    QtWidgets.QMessageBox.information(self, "Kết quả", "Chữ ký hợp lệ!")
                else:
                    QtWidgets.QMessageBox.warning(self, "Kết quả", "Chữ ký không hợp lệ!")
            except:
                QtWidgets.QMessageBox.critical(self, "Lỗi", "Định dạng chữ ký sai!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())