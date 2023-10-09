import unittest
from unittest.mock import patch, MagicMock
from src.server.utils.decrept import Decryption


class TestDecryption(unittest.TestCase):
    @patch("os.getenv", return_value="src/server/.env")
    @patch("rsa.PrivateKey.load_pkcs1")
    @patch("rsa.decrypt", return_value="original_message".encode())
    def test_decrypt_message(self, mock_decrypt, mock_load_pkcs1, mock_getenv):
        mock_private_key = MagicMock()
        mock_load_pkcs1.return_value = mock_private_key
        mock_getenv.return_value = "src/server/.env"

        decryption = Decryption()

        encrypted_result = "encrypted Hello World".encode()
        decrypted_result = decryption.decrypt_message(encrypted_result)

        mock_getenv.assert_called_once_with("PRIVATE_KEY")
        mock_load_pkcs1.assert_called_once_with("src/server/.env")
        mock_decrypt.assert_called_once_with(encrypted_result, mock_private_key)

        self.assertEqual(decrypted_result, "original_message")


if __name__ == "__main__":
    unittest.main()
