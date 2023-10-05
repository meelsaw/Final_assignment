import socket
from config import INPUT_CONFIG
from utils.serialise import Serialiser
from utils.encryption import Encryption


def send_data(data):
    """
    Sends serialised data to the server using socket communication, encrypted if required.

    Parameters:
    - data (dict): A dictionary containing information to be sent.
                The dictionary should include at least the following keys:
                    - "INPUT_STRING" (str): The input string to be sent.
                    - "OUTPUT_TYPE" (str): Indicates the expected output from the server.
                    - "ENCRYPTION" (bool): Indicates whether encryption is enabled.
                    - "PRINT_OUTPUT" (bool): Indicates whether the output string needs to be printed out.
                    - "FILE_OUTPUT" (bool): Indicates whether to save the expected output to a file.

    Returns:
    - str: The received data from the server, converted to the specified data type.
    """

    serialiser = Serialiser()
    encryption = Encryption()
    if data["ENCRYPTION"]:
        data["INPUT_STRING"] = encryption.encrypt_message(data["INPUT_STRING"])

    serialised_data = serialiser.serialise(data)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect(("127.0.0.1", 8888))
        except socket.error as error:
            raise ConnectionError(f"Error connecting to server: {error}") from error

        s.sendall(serialised_data)
        try:
            received_data = serialiser.deserialise(s.recv(1024))

            if not received_data:
                raise ConnectionError("Error: No data received from the server.")

        except socket.error as error:
            raise ConnectionError(
                f"Error receiving data from server: {error}"
            ) from error

    return received_data


data = INPUT_CONFIG
received_string = send_data(data)
print("Received:", received_string)
