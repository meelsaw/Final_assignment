import socket
from config import INPUT_CONFIG
from utils.serialise import Serialiser
from utils.encryption import Encryption


def send_data(data):
    serialiser = Serialiser()
    encryption = Encryption()
    if data["ENCRYPTION"]:
        data["INPUT_STRING"] = encryption.encrypt_message(data["INPUT_STRING"])

    serialised_data = serialiser.serialise(data)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("127.0.0.1", 8888))
        s.sendall(serialised_data)
        received_data = serialiser.deserialise(s.recv(1024))

    return received_data


data = INPUT_CONFIG
received_string = send_data(data)
print("Received:", received_string)
