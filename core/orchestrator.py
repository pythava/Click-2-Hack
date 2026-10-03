from modules import http


def run_modules(target, scan_result):
    results = []

    ports = list(scan_result.keys())

    print(ports)

    for item in ports:
        
        service = scan_result[item]
        print(service)

        if scan_result[item]["state"] != "open":
            continue

        if scan_result[item]["service"] == "http":
            http.main(target, item)
