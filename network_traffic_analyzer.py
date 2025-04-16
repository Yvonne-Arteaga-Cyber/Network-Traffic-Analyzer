# network_traffic_analyzer.py

# This script analyzes Wireshark-exported text logs for suspicious ports

def analyze_logs(file_path):
    suspicious_ports = ["23", "3389", "445"]
    findings = []

    try:
        with open(file_path, "r") as log:
            for line in log:
                for port in suspicious_ports:
                    if f"Port: {port}" in line:
                        findings.append(line.strip())
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return

    if findings:
        print("Suspicious activity detected:\n")
        for f in findings:
            print(f)
    else:
        print("No suspicious ports detected.")

# Example: analyze_logs("wireshark_log.txt")
