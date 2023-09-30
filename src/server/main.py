from utils.serialise import Serialiser
from utils.decrept import Decryption
from utils.file_handler import FileHandler
import socket


def receive_from_client(client_data):
    deserialiser = Serialiser()
    decrypter = Decryption()
    deserialised = deserialiser.deserialise(client_data)
    if deserialised["ENCRYPTION"]:
        decrypted_string = decrypter.decrypt_message(deserialised["INPUT_STRING"])
        if deserialised["PRINT_OUTPUT"]:
            output_str = "The following message received from client:\n {}".format(decrypted_string)
            print(output_str)
            return output_str
        elif deserialised["TEXT_FILE_OUTPUT"]:
            txt = FileHandler.create_txt(input_str=decrypted_string)
            output_file = FileHandler.convert_file(file=txt, format_type=deserialised["OUTPUT_TYPE"])
            return output_file
    else:
        message = deserialised["INPUT_STRING"]
        if deserialised["PRINT_OUTPUT"]:
            output_str = "The following message received from client:\n {}".format(message)
            print(output_str)
            return output_str
        elif deserialised["TEXT_FILE_OUTPUT"]:
            txt = FileHandler.create_txt(input_str=message)
            output_file = FileHandler.convert_file(file=txt, format_type=deserialised["OUTPUT_TYPE"])
            return output_file
    return


def create_listening_socket():
    host = '127.0.0.1'
    port = '12345'
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.bind((host, port))
    socket_server.listen(5)
    while True:
        client_socket, addr = server_socket.accept()
        incoming_data = client_socket.recv(1024)
        client_output = receive_from_client(incoming_data)
        client_socket.send(client_output)
        client_socket.close()
    return
