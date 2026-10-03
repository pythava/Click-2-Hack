import nmap 

def scan_target(target: str) -> list[dict]:
	scanner = nmap.PortScanner()
	
	scanner.scan(
		hosts=target,
		ports="1-65535",
		arguments="-sS -T4 -n -Pn",
	)

	results = []

	for host in scanner.all_hosts():
		for protocol in scanner[host].all_protocols():
			for port, info in scanner[host][protocol].items():
				if info.get("state") != "open":
					continue
				results.append({
					"host": host,
					"port": port,
					"protocol": protocol,
					"state": info["state"],
					"service": info.get("name", "unknown"),
				})
	
	return results

def deep_scan_port(target: str, port) -> list[dict]:
	scanner = nmap.PortScanner()

	scanner.scan(
		hosts=target,
		ports=str(port),
		arguments="-sV -sC -O -v",	
	)

	results =[]

	for host in scanner.all_hosts():
		for protocol in scanner[host].all_protocols():
			for port_num, info in scanner[host][protocol].items():
				results.append({
					"host": host,
					"port": port_num,
					"protocol": protocol,
					"state": info.get("state", "unknown"),
					"service": info.get("name", "unknown"),
					"product": info.get("product", ""),
					"version": info.get("version", ""),
					"extrainfo": info.get("extrainfo", ""),
					"scripts": info.get("script", {}),
				})
	return results
