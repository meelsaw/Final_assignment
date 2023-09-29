import rsa
import os
from dotenv import load_dotenv


class Encryption:
    def encrypt_message(self, message):
        load_dotenv()

        public_key_location = os.getenv("PUBLIC_KEY")
        public_key = rsa.PublicKey.load_pkcs1(public_key_location)

        encrypted_message = rsa.encrypt(message.encode(), public_key)
        return encrypted_message
