"""
    1.Enter a link or a piece of text
    2.if the input is a link. send a request and save the response content to a local file
    3.if that is a text. save it to a local file
    4.Leave an API interface.for the summary module.
"""
import requests
import time

def save_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)

# Generate a unique filename
def generate_unique_filename():
    return str(int(time.time()))

def get_file_content(content):
    if content.startswith('http://', "https://"):
        resp = requests.get(content)
        resp.raise_for_status()
        content = resp.text
    return content


if __name__ == '__main__':
    content = get_file_content(input("Enter a link or piece of text: "))
    
    filename =generate_unique_filename() + '.txt'

    save_file(filename, content)
    