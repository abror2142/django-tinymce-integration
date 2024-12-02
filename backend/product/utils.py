import re
import os

def parse_image_path_from_html(html):
    regex = r'<img[^>]+src=["\'](.*?)["\']' # thank you ChatGPT
    return re.findall(regex, html)

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print("File deleted!")
    else:
        print("File not exists!")