from scapy.all import *
from datetime import datetime
import threading
import subprocess

scan_count = {}
icmp_count = {}

def log_alert(message):
    print(message)

    with open("alerts.log", "a") as f:
        f.write(message + "\n")


def detect(packet):

    # ICMP Detection + ICMP Flood Detection
    if packet.haslayer(IP) and packet.haslayer(ICMP):

        src = packet[IP].src
        dst = packet[IP].dst

        current_time = datetime.now().strftime("%H:%M:%S")

        alert = f"[{current_time}] [ALERT] ICMP Packet Detected: {src} -> {dst}"
        log_alert(alert)

        if src not in icmp_count:
            icmp_count[src] = 0

        icmp_count[src] += 1

        if icmp_count[src] >= 20:

            flood_alert = f"[{current_time}] [ALERT] Possible ICMP Flood Attack From {src}"
            log_alert(flood_alert)

            icmp_count[src] = 0

    # Nmap Scan Detection
    if packet.haslayer(IP) and packet.haslayer(TCP):

        src = packet[IP].src

        if packet[TCP].flags == "S":

            if src not in scan_count:
                scan_count[src] = 0

            scan_count[src] += 1

            if scan_count[src] >= 3:

                current_time = datetime.now().strftime("%H:%M:%S")

                alert = f"[{current_time}] [ALERT] Possible Nmap Scan From {src}"
                log_alert(alert)

                scan_count[src] = 0


def monitor_ssh():

    process = subprocess.Popen(
        ["journalctl", "-fu", "ssh"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    for line in process.stdout:

        if "Failed password" in line:

            current_time = datetime.now().strftime("%H:%M:%S")

            alert = f"[{current_time}] [ALERT] SSH Brute Force Attempt Detected"
            log_alert(alert)


print("=" * 50)
print("Mini IDS Started...")
print("Features Enabled:")
print("1. ICMP Detection")
print("2. ICMP Flood Detection")
print("3. Nmap Scan Detection")
print("4. SSH Brute Force Detection")
print("=" * 50)

ssh_thread = threading.Thread(target=monitor_ssh, daemon=True)
ssh_thread.start()

sniff(iface="eth0", prn=detect, store=False)
