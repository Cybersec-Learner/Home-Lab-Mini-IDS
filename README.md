# Home Lab Mini IDS

## Overview

This project is a Python-based Mini Intrusion Detection System (IDS) developed in a Kali Linux home lab environment. The IDS monitors network traffic, detects suspicious activities, and generates real-time security alerts.

## Features

* ICMP Packet Detection
* ICMP Flood Attack Detection
* Nmap Scan Detection
* SSH Brute Force Detection
* IDS Shows Brute Force Alerts
* Real-Time Alert Generation
* Alert Logging and Monitoring

## Technologies Used

* Python 3
* Scapy
* Kali Linux
* Threading
* Subprocess

## Project Structure

```text
Home-Lab-Mini-IDS/
├── ids.py
├── README.md
```

## Running the Project

```bash
sudo python3 ids.py
```

## Detection Capabilities

### ICMP Detection

The IDS monitors ICMP traffic and logs packet activity between hosts.

<img width="1291" height="689" alt="IDS detect ICMP packets   show  Alert" src="https://github.com/user-attachments/assets/b57113f2-7439-42fc-9b7f-aba1148b9302" />

### ICMP Flood Detection

The system generates alerts when excessive ICMP packets are detected from a single source.

<img width="1287" height="470" alt="IDS show ICMP flood  Alert" src="https://github.com/user-attachments/assets/ab6039b7-9100-4bc3-9b14-02ead5edf14a" />


### Nmap Scan Detection

The IDS detects suspicious TCP SYN scan behavior that may indicate network reconnaissance activity.

<img width="1284" height="920" alt="Mini IDS scan Nmap   ICMP packet detected" src="https://github.com/user-attachments/assets/03e5b3b5-cf16-4dca-955e-34a6bef48882" />


### SSH Brute Force Detection

The IDS monitors SSH authentication logs and alerts on repeated failed login attempts.

<img width="1289" height="1019" alt="IDS detect Brute Force" src="https://github.com/user-attachments/assets/e9810809-d86e-4a86-a81f-33e97c50c9ab" />


### Brute Force Alert Monitoring

The IDS displays and logs brute force attack alerts in real time, helping users identify unauthorized login attempts and suspicious authentication activity.

<img width="1300" height="1013" alt="IDS show Brute Force  Alert" src="https://github.com/user-attachments/assets/fde3964e-a023-4549-9cdb-ddacc25bbdd6" />


## Authors

* Muhammad Adeel
* Abdullah Naeem

## Educational Purpose

This project was developed for cybersecurity learning, network monitoring, and home lab testing purposes.
