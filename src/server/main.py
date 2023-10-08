"""Module enables socket creation and listen to client"""
import socket
"""Module enables str conversion to json"""
import json
"""Module enables str conversion to xml"""
import xml.etree.ElementTree as ET
from utils.serialise import Serialiser
from utils.decrept import Decryption
from utils.file_handler import FileHandler


def create_file(input_data, format_input):
    """
    Helper function that creates a txt file then convertes it to the desired format
    :param input_data: str to be written into output file
    :param format_input: str discribing requested file format of XML/JSON/BINARY
    :return: XML/JSON/BINARY file
    """
    filehandler = FileHandler()
    txt = filehandler.create_txt(input_str=input_data)
    output_file = filehandler.convert_file(file=txt, format_type=format_input)
    return output_file


def print_json(data):
    """
    Helper function prints data in json format
    :param client message
    """
    try:
        formatted_json = json.dumps(data, indent=4)
        print(formatted_json)
    except Exception as e:
        return str(e)


def print_xml(data):
    """
    Helper function prints data in xml format
    :param client message
    """
    try:
        root = ET.Element("root")
        element = ET.SubElement(root, "message")
        element.text = data
        tree = ET.ElementTree(root)
        xml_string = ET.tostring(root, encoding="utf-8", method="xml")
        print(xml_string)
    except Exception as e:
        return str(e)


def print_binary(data):
    """
    Helper function prints data in binary format
    :param client message
    """
    try:
        binary_data = data.encode("utf-8")
        for byte in binary_data:
            print(bin(byte)[2:].zfill(8), end=" ")
    except Exception as e:
        return str(e)


def print_out(data, output_type):
    """
    A function that prints str in requested format
    :param data: message from client
    :param output_type: "BINARY" or "JSON" or "XML"
    """
    if output_type == "JSON":
        print_json(data)
    elif output_type == "XML":
        print_xml(data)
    elif output_type == "BINARY":
        print_binary(data)
    else:
        print("Format type not supported")
    return


def receive_from_client(client_data):
    """
    Main function that process data sent from the client
    :param client_data: config dict sent from client
    :return: JSON or XML or BIN file based on client request
    """
    deserialiser = Serialiser()
    decrypter = Decryption()
    deserialised = deserialiser.deserialise(client_data)
    if deserialised["ENCRYPTION"]:
        decrypted_string = decrypter.decrypt_message(deserialised["INPUT_STRING"])
        if deserialised["PRINT_OUTPUT"] and deserialised["FILE_OUTPUT"]:
            print_output = (f"The following data received from client:\n {decrypted_string}"
                            f"\n Printing in requested format:\n")
            print_out(decrypted_string, deserialised["OUTPUT_TYPE"])
            requested_output = create_file(input_data=decrypted_string,
                                           format_input=deserialised["OUTPUT_TYPE"])
            print(print_output)
        elif deserialised["PRINT_OUTPUT"]:
            requested_output = (f"The following data received from client:\n {decrypted_string}"
                                f"\n Printing in requested format:\n")
            print(requested_output)
            print_out(decrypted_string, deserialised["OUTPUT_TYPE"])
        elif deserialised["FILE_OUTPUT"]:
            requested_output = create_file(input_data=decrypted_string,
                                            format_input=deserialised["OUTPUT_TYPE"])
        else:
            print("Request not supported")
    else:
        message = deserialised["INPUT_STRING"]
        if deserialised["PRINT_OUTPUT"] and deserialised["FILE_OUTPUT"]:
            print(f"The following data received from client:\n {message}"
                  f"\n Printing in requested format:\n")
            print_out(message, deserialised["OUTPUT_TYPE"])
            requested_output = create_file(input_data=message,
                                           format_input=deserialised["OUTPUT_TYPE"])
        elif deserialised["PRINT_OUTPUT"]:
            requested_output = (f"The following data received from client:\n {message}"
                                f"\n Printing in requested format:\n")
            print(requested_output)
            print_out(message, deserialised["OUTPUT_TYPE"])
        elif deserialised["FILE_OUTPUT"]:
            requested_output = create_file(input_data=message,
                                            format_input=deserialised["OUTPUT_TYPE"])
        else:
            print("Request not supported")
    return deserialiser.serialise(requested_output)

def create_listening_socket():
    """
    A function that creates a socket server and listents to max 5 clients
    When client connection is established, it calls the main processing function
    """
    host = '127.0.0.1'
    port = 8888
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.bind((host, port))
    socket_server.listen(5)
    print(f"Server listening on {host}:{port}")
    while True:
        client_socket, addr = socket_server.accept()
        print(f"Accepted connection from {addr}")
        incoming_data = client_socket.recv(1024)
        client_output = receive_from_client(incoming_data)
        client_socket.send(client_output)
        client_socket.close()

if __name__=="__main__":
    create_listening_socket()
