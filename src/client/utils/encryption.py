import rsa
import os
from dotenv import load_dotenv


class Encryption:
    def encrypt_message(self, message):
        """
        Encrypts the message using RSA encryption.

        Parameters:
        - message (str): The message that needs to be encrypted.

        Returns:
        - bytes: returns the encrypted message.


        """

        load_dotenv()

        public_key_location = os.getenv("PUBLIC_KEY")
        if not public_key_location:
            raise ValueError("public_key_location cannot be found")

        try:
            public_key = rsa.PublicKey.load_pkcs1(public_key_location)

        except Exception as error:
            raise ValueError(f"Error: {error}") from error

        try:
            encrypted_message = rsa.encrypt(message.encode(), public_key)
            return encrypted_message
        except Exception as error:
            raise ValueError(f"Error: {error}") from error
