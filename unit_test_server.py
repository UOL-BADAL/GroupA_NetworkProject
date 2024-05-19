#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pytest
from fastapi.testclient import TestClient
from server import app
from utils import serialiser, encrypter

unit_test_client = TestClient(app)

def test_root_endpoint_get():
    """
    Test the root endpoint to ensure it returns the message "Hello World".
    """
    response = unit_test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_data_post_json_print():
    """
    Test the /data endpoint with JSON payload and print option.
    """
    os.environ["PRINT_OR_SAVE"] = "1"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "payload": '{"name": "test"}',
        "payload_format": "JSON"
    }
    response = unit_test_client.post("/data", data=data, headers=headers)
    assert response.status_code == 200
    assert response.json() == {"status": "success"}

def test_data_post_binary_print():
    """
    Test the /data endpoint with binary payload and print option.
    """
    os.environ["PRINT_OR_SAVE"] = "1"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    binary_payload = serialiser.dictionary_to_binary({"name": "test"}).decode()
    data = {
        "payload": binary_payload,
        "payload_format": "BINARY"
    }
    response = unit_test_client.post("/data", data=data, headers=headers)
    assert response.status_code == 200
    assert response.json() == {"status": "success"}

def test_data_post_xml_print():
    """
    Test the /data endpoint with XML payload and print option.
    """
    os.environ["PRINT_OR_SAVE"] = "1"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    xml_payload = serialiser.dictionary_to_xml({"name": "test"}).decode()
    data = {
        "payload": xml_payload,
        "payload_format": "XML"
    }
    response = unit_test_client.post("/data", data=data, headers=headers)
    assert response.status_code == 200
    assert response.json() == {"status": "success"}

def test_data_post_unsupported_format():
    """
    Test the /data endpoint with an unsupported format to ensure it returns an error.
    """
    os.environ["PRINT_OR_SAVE"] = "1"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "payload": '{"name": "test"}',
        "payload_format": "UNSUPPORTED"
    }
    response = unit_test_client.post("/data", data=data, headers=headers)
    assert response.status_code == 400
    assert response.json() == {"detail": "Unsupported format"}

def test_file_post_no_encryption():
    """
    Test the /file endpoint with file content and no encryption.
    """
    os.environ["PRINT_OR_SAVE"] = "1"  # Set to "print"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "file_content": "This is a test file content."
    }
    response = unit_test_client.post("/file", data=data, headers=headers)
    assert response.status_code == 200
    assert response.json() == {"status": "success"}

def test_file_post_with_encryption():
    """
    Test the /file endpoint with file content and encryption.
    """
    os.environ["PRINT_OR_SAVE"] = "1"
    encryption_key = "unit_test"
    encryption_key, encrypted_content = encrypter.encrypt("This is a test file content.")
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "encryption_key": encryption_key
    }
    data = {
        "file_content": encrypted_content.decode()
    }
    response = unit_test_client.post("/file", data=data, headers=headers)
    assert response.status_code == 200
    assert response.json() == {"status": "success"}
    
def test_file_post_missing_content():
    """
    Test the /file endpoint with missing file content to ensure it returns an error.
    """
    os.environ["PRINT_OR_SAVE"] = "1" 
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {}
    response = unit_test_client.post("/file", data=data, headers=headers)
    assert response.status_code == 400
    assert response.json() == {"detail": "File content is required"}


# In[ ]:




