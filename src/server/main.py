"""Module enables socket creation and listen to client"""
import socket
from utils.serialise import Serialiser
from utils.decrept import Decryption
from utils.file_handler import FileHandler


def convert_file(input_data, format_input):
    """
    Helper function that creates a txt file then convertes it to the desired format
    """
    txt = FileHandler.create_txt(input_str=input_data)
    output_file = FileHandler.convert_file(file=txt, format_type=format_input)
    return output_file


def receive_from_client(client_data):
    """
    Main function that process data sent from the client
    """
    deserialiser = Serialiser()
    decrypter = Decryption()
    deserialised = deserialiser.deserialise(client_data)
    if deserialised["ENCRYPTION"]:
        decrypted_string = decrypter.decrypt_message(deserialised["INPUT_STRING"])
        if deserialised["PRINT_OUTPUT"]:
            requested_output = f"The following message received from client:\n {decrypted_string}"
            print(requested_output)
        elif deserialised["TEXT_FILE_OUTPUT"]:
            requested_output = convert_file(input_data=decrypted_string,
                                            format_input=deserialised["OUTPUT_TYPE"])
        else:
            print("Request not supported")
    else:
        message = deserialised["INPUT_STRING"]
        if deserialised["PRINT_OUTPUT"]:
            requested_output = f"The following message received from client:\n {message}"
            print(requested_output)
        elif deserialised["TEXT_FILE_OUTPUT"]:
            requested_output = convert_file(input_data=message,
                                            format_input=deserialised["OUTPUT_TYPE"])
        else:
            print("Request not supported")
    return requested_output

def create_listening_socket():
    """
    A function that creates a socket server and listents to max 5 clients
    When client connection is established, it calls the main processing function
    """
    host = '127.0.0.1'
    port = '8888'
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.bind((host, port))
    socket_server.listen(5)
    while True:
        client_socket, addr = socket_server.accept()
        print(f"Accepted connection from {addr}")
        incoming_data = client_socket.recv(1024)
        client_output = receive_from_client(incoming_data)
        client_socket.send(client_output)
        client_socket.close()

if __name__=="__main__":
    create_listening_socket()
