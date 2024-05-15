from fastapi import FastAPI, Request
import uvicorn
import sys
import utils.file_handler as fh
from utils import serialiser, encrypter


# Port number defined
port = 8000

# Ask user for printing or saving preference
print_or_save = input("If you want to print select 1, if you want to save select 2, if you want to print and save select 3")

# Map user input
if print_or_save == "1":
   print_or_save = "print"
elif print_or_save == "2":
   print_or_save = "save"
elif print_or_save == "3":
   print_or_save = "both"
else:
   print("Please select a valid option")
   sys.exit()

# Create FastAPI
app = FastAPI()


# Deine root endpoint
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Define endpoint for receiving data
@app.post("/data")
async def root_post(request: Request):
    data = await request.form()
    serialised_data = data.get("payload")
    format = data.get("payload_format")

    # Deserialise data based on format
    if format == "JSON":
        raw_dictionary = serialiser.json_to_dictionary(serialised_data)
    elif format == "BINARY":
        serialised_data = serialised_data.encode()
        raw_dictionary = serialiser.binary_to_dictionary(serialised_data)
    elif format == "XML":
        serialised_data = serialised_data.encode()
        raw_dictionary = serialiser.xml_to_dictionary(serialised_data)

    # Print or save data based on user preference 
    if print_or_save in ["print", "both"]:
        print(raw_dictionary)

    if print_or_save in ["save", "both"]:
        fh.write("server_file.txt", str(raw_dictionary))

# Define endpoint for receiving files
@app.post("/file")
async def root_file(request: Request):
    data = await request.form()
    headers = dict(request.headers)
    file_content = data.get("file_content")
    encryption_key = headers.get("encryption_key")

    # Define file content if encryption key is provided
    if encryption_key:
        encryption_key = encryption_key.encode()
        file_content = file_content.encode()
        file_content = encrypter.decrypt(file_content, encryption_key)
    print(file_content, type(file_content)) # ##Missing some code (hacer lo mismo del endpoint de arrible line 43-47)

# Run the FastAPI app 
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port, loop="asyncio")