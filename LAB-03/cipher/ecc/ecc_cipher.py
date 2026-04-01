import ecdsa, os, sys
from PyQt5 import QtWidgets

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from ui.ecc import Ui_Dialog

if not os.path.exists('cipher/ecc/keys'):
    os.makedirs('cipher/ecc/keys')

class ECCCipher:
    def __init__(self):
        pass

    def generate_keys(self):
        sk = ecdsa.SigningKey.generate()
        vk = sk.get_verifying_key()
        
        with open('cipher/ecc/keys/privateKey.pem', 'wb') as p:
            p.write(sk.to_pem())
            
        with open('cipher/ecc/keys/publicKey.pem', 'wb') as p:
            p.write(vk.to_pem())

    def load_keys(self):
        with open('cipher/ecc/keys/privateKey.pem', 'rb') as p:
            sk = ecdsa.SigningKey.from_pem(p.read())
            
        with open('cipher/ecc/keys/publicKey.pem', 'rb') as p:
            vk = ecdsa.VerifyingKey.from_pem(p.read())
            
        return sk, vk

    def sign(self, message, key):
        return key.sign(message.encode('utf-8'))

    def verify(self, message, signature, key):
        _, vk = self.load_keys()
        try:
            return vk.verify(signature, message.encode('utf-8'))
        except ecdsa.BadSignatureError:
            return False

class MainApp(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ecc_cipher = ECCCipher()
        
        if not os.path.exists('cipher/ecc/keys/privateKey.pem'):
            self.ecc_cipher.generate_keys()
        
        self.ui.pushButton.clicked.connect(self.handle_sign)
        self.ui.pushButton_2.clicked.connect(self.handle_verify)
        self.ui.pushButton_3.clicked.connect(self.handle_generate_keys)

    def handle_generate_keys(self):
        self.ecc_cipher.generate_keys()
        QtWidgets.QMessageBox.information(self, "Thành công", "Đã tạo bộ khóa ECC mới!")

    def handle_sign(self):
        message = self.ui.textEdit.toPlainText()
        if message:
            private_key, _ = self.ecc_cipher.load_keys()
            signature = self.ecc_cipher.sign(message, private_key)
            self.ui.textEdit_2.setPlainText(signature.hex())

    def handle_verify(self):
        message = self.ui.textEdit.toPlainText()
        sig_hex = self.ui.textEdit_2.toPlainText()
        if message and sig_hex:
            _, public_key = self.ecc_cipher.load_keys()
            try:
                signature = bytes.fromhex(sig_hex)
                is_valid = self.ecc_cipher.verify(message, signature, public_key)
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