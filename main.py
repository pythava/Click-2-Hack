from core import port_scanner, logging, orchestrator
import time


ip = input("Target_IP > ")

open_port_result = port_scanner.scan_target(ip)

for item in open_port_result:
	service = item["service"]
	port = item["port"]

	print(f"[port] : {port}\n[service] : {service}\n")

	logging.log(f"time={time.time()} | [port] : {port}\n[service] : {service}\n")

print(f"[+] {len(open_port_result)} Port is Opened")
print("[*] Depp Scanning ports...")

deep_scan_result = []

for item in open_port_result:
	port = item["port"]
	deep_scan_result.extend(port_scanner.deep_scan_port(ip, port))

ip_info={}

for item in deep_scan_result:
	port = item["port"]
	ip_info[port] = {
		"service":item["service"],
		"version":item["version"],
		"state":item["state"]
	}

orchestrator.run_modules(ip, ip_info)