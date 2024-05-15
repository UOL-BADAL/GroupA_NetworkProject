from utils import file_handler, serialiser, encrypter
import sys
import requests

# Server conection URL
server_url = "http://localhost:8000" 

# Define file name
file_name = "client_file.txt"

# Create a dictionary
my_dict = {"artist_name": "Rihanna", "real_name": "Robyn Rihanna Fenty", "nationality": "Barbadian", "age": 36} 

print ("Dictionary created")

try:
    # Write sample text to file and read it back 
    file_handler.write(file_name, "client example text")
    file_content = file_handler.read(file_name)
    print ("Text file created successfully")

except Exception as e:
    # Handle error if file creation fails
    print ("error occured while created file: "+ str(e))
    sys.exit()

try:
    # Ask user to select serialisation format
    serialisation_format = input("Enter 1 to convert to JSON, 2 to convert to BINARY, or 3 to convert XML: ") 
    if serialisation_format == "1": # Convert dictionary to JSON
        serialised_data = serialiser.dictionary_to_json(my_dict)
        serialisation_format = "JSON"
    elif serialisation_format == "2": # Convert dictionary to binary
        serialised_data = serialiser.dictionary_to_binary(my_dict)
        serialisation_format = "BINARY"
    elif serialisation_format == "3": # Convert dictionary to XML
        serialised_data = serialiser.dictionary_to_xml(my_dict)
        serialisation_format = "XML"
    else:
        # Handle invalid format input
        print("Invalid convert format"+ str(e))
        sys.exit()
except Exception as e:
    # Handle error during serialisation
    print("Error while converting the dictionary"+ str(e))
    sys.exit()

try:
    # Ask the user whether to encrypt the text file
    is_encrypted = input("Encrypt text file? y/n: ")
    is_encrypted = is_encrypted.lower()
    if is_encrypted != "y" and is_encrypted != "n":
        # Handle invalid input
        print ("invalid encrypt input")   
        sys.exit() 
    if is_encrypted == "y": # Encrypt file content if requested
        encryption_key, file_content_to_send = encrypter.encrypt(file_content)
    else:
        # If not encrypting, set encryption ley to empty and use original file content 
        encryption_key = b""
        file_content_to_send = file_content
except Exception as e:
    # Handle error during encryption
    print("Error while encrypting"+ str(e))
    sys.exit()

try:
    # Send serialised data and file content to the server
    response = requests.post( 
        server_url+"/data",
        data={
            "payload": serialised_data,
            #"encyption_key": encryption_key,
            "payload_format": serialisation_format
        },
        # files={
        #     "upload_file": file_content_to_send
        # },
        timeout=60
    )
    response = requests.post( 
        server_url+"/file",
        headers={
            "encryption_key": encryption_key,
        },
        data={
            "file_content": file_content_to_send
        },
        timeout=60
    ) 
except Exception as e:
    # Handle error while sending data to server
    print("Error while sending to server"+ str(e))
    sys.exit()