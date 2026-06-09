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
├── ids_icmp.py
├── README.md
└── screenshots/
```

## Running the Project

```bash
sudo python3 ids.py
```

## Detection Capabilities

### ICMP Detection

The IDS monitors ICMP traffic and logs packet activity between hosts.

### ICMP Flood Detection

The system generates alerts when excessive ICMP packets are detected from a single source.

### Nmap Scan Detection

The IDS detects suspicious TCP SYN scan behavior that may indicate network reconnaissance activity.

### SSH Brute Force Detection

The IDS monitors SSH authentication logs and alerts on repeated failed login attempts.

### Brute Force Alert Monitoring

The IDS displays and logs brute force attack alerts in real time, helping users identify unauthorized login attempts and suspicious authentication activity.

## Screenshots

Add project screenshots in the `screenshots` folder and reference them here.

## Authors

* Muhammad Adeel
* Abdullah Naeem

## Educational Purpose

This project was developed for cybersecurity learning, network monitoring, and home lab testing purposes.
