import requests
from datetime import datetime, timezone
from bs4 import BeautifulSoup
from core import dir_scanner
from config import WEB_WORDLIST_DIR

def main(target, port):
    print(f"===[Scaning http://{target}:{port}]==========================\n")

    url = f"http://{target}:{port}"
    wordlist = WEB_WORDLIST_DIR

    returned = dir_scanner.scan_directories(url, wordlist)

    try:
        res = requests.get(url)
        #print(res.content.decode("utf-8"))
        
    except:
        print("errrrrrrrrrrrrror")
