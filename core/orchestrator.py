from modules import http


def run_modules(target, scan_result):
    results = []

    ports = list(scan_result.keys())

    for item in ports:

        if scan_result[item]["state"] != "open":
            continue

        if scan_result[item]["service"] == "http":
            http.main(target, item)
