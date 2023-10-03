import unittest
from unittest.mock import patch, MagicMock
from src.client.utils.encryption import Encryption


class TestEncryption(unittest.TestCase):
    @patch("os.getenv", return_value="src/client/.env")
    @patch("rsa.PublicKey.load_pkcs1")
    @patch("rsa.encrypt", return_value="encrypted Hello World".encode())
    def test_encrypt_message(self, mock_encrypt, mock_load_pkcs1, mock_getenv):
        mock_public_key = MagicMock()
        mock_load_pkcs1.return_value = mock_public_key
        mock_getenv.return_value = "src/client/.env"

        encryption = Encryption()

        original_message = "original_message"
        result = encryption.encrypt_message(original_message)

        mock_getenv.assert_called_once_with("PUBLIC_KEY")
        mock_load_pkcs1.assert_called_once_with("src/client/.env")
        mock_encrypt.assert_called_once_with(original_message.encode(), mock_public_key)

        self.assertEqual(result, "encrypted Hello World".encode())


if __name__ == "__main__":
    unittest.main()
