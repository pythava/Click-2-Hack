import requests
from urllib.parse import urljoin 

def scan_directories(base_url, wordlist_path):
    base_url = base_url.rstrip("/") + "/"

    with open(wordlist_path, "r", encoding="utf-8") as file:
        paths = [
            line.strip()
            for line in file
            if line.strip() and not line.lstrip().startswith("#")
        ]

    results = []

    with requests.Session() as session:
        for path in paths:
            target_url = urljoin(base_url, path)

            try:
                res = session.get(target_url, timeout=5, allow_redirects=False)

                if res.status_code in (200, 204, 301, 302, 401, 403):
                    result = {
                        "url": target_url,
                        "status": res.status_code,
                        "size": len(res.content)
                    }

                    results.append(result)

                    print(f"[{res.status_code}] - {target_url}\t\t | {len(res.content)} bytes")

            except requests.RequestException as error:
                print(f"[ERROR] {target_url}: {error}")


    print("\n")
    return results