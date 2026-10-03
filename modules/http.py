import requests
import ssl
import socket
from datetime import datetime, timezone

def main(target, port):
    url = f"http://{target}:{port}"

    try:
        res = requests.get(url)
        print(res.content.decode("utf-8"))
    except:
        print("errrrrrrrrrrrrror")
