import os
import socket
from config import INPUT_CONFIG
from utils.serialise import Serialiser
from utils.encryption import Encryption


def download_file(file_path):
    """
    Download file from a given file path and save it to the current directory

    Parameters:
    - data (str): File path received from the server

    """
    with open(file_path, "rb") as file:
        local_file_name = os.path.basename(file_path)
        local_file_path = os.path.join(".", local_file_name)
        with open(local_file_path, "wb") as local_file:
            local_file.write(file.read())
    print(f"File saved at {local_file_path}")


def send_data(data):
    """
    Sends serialised data to the server using socket communication, encrypted if required.

    Parameters:
    - data (dict): A dictionary containing information to be sent.
                The dictionary should include at least the following keys:
                    - "INPUT_STRING" (str): The input string to be sent.
                    - "OUTPUT_TYPE" (str): Indicates the expected output from the server.
                    - "ENCRYPTION" (bool): Indicates whether encryption is enabled.
                    - "PRINT_OUTPUT" (bool): Indicates whether the output needs to be printed out.
                    - "FILE_OUTPUT" (bool): Indicates whether to save the expected output to a file.

    Returns:
    - str: The received data from the server, converted to the specified data type.
    """

    serialiser = Serialiser()
    encryption = Encryption()
    if data["ENCRYPTION"]:
        data["INPUT_STRING"] = encryption.encrypt_message(data["INPUT_STRING"])

    serialised_data = serialiser.serialise(data)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        try:
            server.connect(("127.0.0.1", 8888))
        except socket.error as error:
            raise ConnectionError(f"Error connecting to server: {error}") from error

        server.sendall(serialised_data)
        try:
            received_data = serialiser.deserialise(server.recv(1024))

            if not received_data:
                raise ConnectionError("Error: No data received from the server.")

            if os.path.exists(received_data):
                download_file(received_data)
            else:
                print("Received from server:", received_data)

        except socket.error as error:
            raise ConnectionError(
                f"Error receiving data from server: {error}"
            ) from error

    return received_data


input_data = INPUT_CONFIG
received_string = send_data(input_data)
