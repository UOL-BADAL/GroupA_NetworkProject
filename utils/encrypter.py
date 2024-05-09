from cryptography.fernet import Fernet

def encrypt(text_file_content: str): 
    """
    Params:
        - text_file_content: str -> text to encrypt
    Returns: 
        - encryption_key: bytes -> encryption key
        - text_file_encrypted: bytes -> encrypted text 
    """
    encryption_key = Fernet.generate_key()
    fernet = Fernet(encryption_key) 
    text_file_encrypted = fernet.encrypt(bytes(text_file_content, encoding="utf-8"))
    return encryption_key, text_file_encrypted

def decrypt(text_file_encrypted: bytes, key: bytes):
    """
    Params:
        - text_file_encrypted: bytes -> text to decrypt
        - key: bytes -> encryption key
    Returns: 
        - text_file_content: str -> decrypted text
    """
    fernet = Fernet(key)
    text_file_content = fernet.decrypt(text_file_encrypted).decode("utf-8")
    return text_file_content
