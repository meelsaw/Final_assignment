import rsa
import os
from dotenv import load_dotenv


class Decryption:
    def decrypt_message(self, message):
        """
        Decrypts the message using RSA encryption.
        :param message (str): The message that needs to be decrypted.
        :return: returns the decrypted message.
        """
        load_dotenv()

        private_key_location = os.getenv("PRIVATE_KEY")
        private_key = rsa.PrivateKey.load_pkcs1(private_key_location)

        decrypted_message = rsa.decrypt(message, private_key)
        return decrypted_message.decode('utf-8')
