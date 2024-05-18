# GroupA_NetworkProject
# About This Project: Client/Server Network System

## Overview

Welcome to the Client/Server Network System project! This project demonstrates a simple client/server architecture where the client application can create, serialise, and optionally encrypt data before sending it to the server. The server then processes the received data, providing options to either print it to the console or save it to a file.

## Features

- **Dictionary Serialisation**: The client can serialise dictionaries into multiple formats, including JSON, binary, and XML.
- **File Encryption**: Optionally encrypt text files before sending them to the server to ensure data security.
- **Configurable Server**: The server can be configured to print or save the processed data based on user preferences.
- **Comprehensive Testing**: Unit tests and feature tests ensure the system's reliability and correctness.

## Architecture

- **Client Application (`client.py`)**:
  - Creates and serialises a dictionary.
  - Optionally encrypts a text file.
  - Sends the serialised dictionary and text file to the server.
  - Handles user input for serialisation format and encryption.

- **Server Application (`server.py`)**:
  - Receives serialised data and text files from the client.
  - Deserialises the received dictionary based on its format.
  - Decrypts the received text file if it was encrypted.
  - Prints or saves the processed data based on user configuration.

- **Utility Modules**:
  - **`encrypter.py`**: Handles encryption and decryption of text files.
  - **`file_handler.py`**: Provides functions to read from and write to text files.
  - **`serialiser.py`**: Contains functions to serialise and deserialise dictionaries in binary, JSON, and XML formats.

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/client-server-network-system.git
   cd client-server-network-system



2. Install Dependencies:
   ```bash
   pip install -r requirements.txt


3.Start the Server:
  ```bash
  python server.py


4.Run the Client:
  ```bash
  python client.py


- ##Usage

- Follow the prompts in the client application to select the serialisation format and encryption option.
- The server will handle the received data based on the configuration set at startup.

- ##Testing

- **Unit Tests**: Ensure the correctness of individual components.
- **Feature Tests**: Validate the end-to-end functionality of the system.





Run the tests using:
```bash
pytest
