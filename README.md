# Project Title: Simple Client/Server Network

## Description

This project involves building a simple client/server network for a secure application. Users can send message through in dictionary with configurable serialisation formats (binary, JSON, XML) and encryption options.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Repository](#repository)
- [License](#license)

## Installation

To install the necessary dependencies for the application, use the following command:


````
pip3 install -r requirements.txt
````

This will ensure that the required libraries are installed to run the application successfully.

## Usage

The application consists of two parts: the client and the server, it allows users to securely exchange messages in a dictionary.

### Server
To run the server, execute the following command:
````
python3 src/server/main.py
````
This command will start the server, and it will be ready to accept connections from clients.

### Client
To run the client, execute the following command:

````
python3 src/client/main.py
````

This command will launch the client application, allowing users to connect to the server and send messages securely. Users can create messages as dictionaries with options such as encryption, decryption, printing, and exporting to a file.

The message will be processed by the server based on the specified options. The server will handle encrypted content and print or export the messages accordingly.

## Testing

To run all tests for the application, use the following command:

````
python3 -m unittest discover -s tests
````

This command will discover and run tests for various modules inside the "tests" directory, including subdirectories. The tests cover encryption (test_encryption), serialisation (test_serialiser), and file handling (test_file_handler), among others.


## Repository

Find more details in  [GitHub repository](https://github.com/meelsaw/Final_assignment).


## License

This project is licensed under the MIT License. 

