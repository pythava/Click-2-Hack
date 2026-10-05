from core import port_scanner, logging, orchestrator, parser
import time
from pathlib import Path
from config import PORT_INFO_DIR

ip = input("Target_IP > ")

if Path(PORT_INFO_DIR).exists():
	print(f"\n[!] {PORT_INFO_DIR} exist do you want use {PORT_INFO_DIR}? (Y / N)")
	ans = input("C2H > ")
	print("\n")

	if ans == "Y" or ans =="y":
		ip_info = parser.load_port_info(PORT_INFO_DIR)

	elif ans == "N" or ans == "n":
		print("===[Port Scanning Start]=============================\n")
		open_port_result = port_scanner.scan_target(ip)

		for item in open_port_result:
			service = item["service"]
			port = item["port"]

			print(f"[port] : {port}\n[service] : {service}\n")

			logging.log(f"time={time.time()} | [port] : {port}\n[service] : {service}\n")

		print(f"[+] {len(open_port_result)} Port is Opened\n")
		print("===[Depp Scanning ports...]==========================\n")

		deep_scan_result = []

		for item in open_port_result:
			port = item["port"]
			deep_scan_result.extend(port_scanner.deep_scan_port(ip, port))

		for deep_scan_port in deep_scan_result:
			print("\n" + "=" * 50)
			print(f"Host       : {deep_scan_port['host']}")
			print(f"Port       : {deep_scan_port['port']}/{deep_scan_port['protocol']}")
			print(f"State      : {deep_scan_port['state']}")
			print(f"Service    : {deep_scan_port['service']}")
			print(f"Product    : {deep_scan_port['product'] or 'Unknown'}")
			print(f"Version    : {deep_scan_port['version'] or 'Unknown'}")
			print(f"Extra Info : {deep_scan_port['extrainfo'] or 'None'}")

			print("Scripts    :")
			if deep_scan_port['scripts']:
				for script_name, script_output in deep_scan_port['scripts'].items():
					print(f"  - {script_name}:")
					print(f"    {script_output.strip()}")
			else:
				print("  None")

		print("\n")

		ip_info={}

		for item in deep_scan_result:
			port = item["port"]
			ip_info[port] = {
				"service":item["service"],
				"version":item["version"],
				"state":item["state"]
			}
	else:
		print("wrong ans")

orchestrator.run_modules(ip, ip_info)