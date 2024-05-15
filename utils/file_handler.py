def read(file_name: str):
    """
    Params:
        - file_name: str -> file to read
    Returns
        - contents: str -> the contents of the file as a string
    """
    with open(file_name, "r") as f:
        contents = f.read()
    return contents

def write(file_name: str, file_text: str):
    """
    Params:
        - file_name: str -> file to write to
        - file_text: str -> text to write to the file
    """
    with open(file_name, "w") as f:
        f.write(file_text)