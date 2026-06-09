from scapy.all import *
from datetime import datetime

def detect(packet):

    if packet.haslayer(IP) and packet.haslayer(ICMP):

        src = packet[IP].src
        dst = packet[IP].dst

        current_time = datetime.now().strftime("%H:%M:%S")

        alert = f"[{current_time}] [ALERT] ICMP Packet Detected: {src} -> {dst}"

        print(alert)

        with open("alerts.log", "a") as f:
            f.write(alert + "\n")

print("Mini IDS Started...")
sniff(prn=detect, store=False)
