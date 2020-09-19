from cryptography.fernet import Fernet


class Key:

    def __init__(self, key=""):
        self.key=key

    def generate_key(self):
        self.key = Fernet.generate_key()

    def encrypt_message(self, message=""):
        message = message.encode()
        key = Fernet(self.key)
        return key.encrypt(message)      

    def decrypt_message(self, message=""):
        key = Fernet(self.key)
        return key.decrypt(message).decode("utf-8")

    def save_key(self):
        key = Fernet.generate_key()
        with open("key", "wb") as key_file:
            key_file.write(key)

    def load_key(self):
        return Fernet(open("key", "rb").read())
        