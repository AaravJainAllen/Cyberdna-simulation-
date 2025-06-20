# CyberDNA - Enhanced Console-Based Simulation with Animation and Styling
# Simulates behavior monitoring with visual feedback and containment actions

import time
import random
import os
import json
from datetime import datetime

# Define color codes for console (works on most terminals)
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# --- Healthy system baseline ---
baseline = {
    "cpu_usage": (10, 15),
    "network_activity": (20, 40),
    "file_access_rate": (0, 3)
}

# Clear console for better animation feel
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Simulate system behavior
def simulate_behavior(cycle, total):
    if cycle == total - 1:
        # Final cycle: return safe values
        return {
            "cpu_usage": 12,
            "network_activity": 30,
            "file_access_rate": 1
        }
    else:
        return {
            "cpu_usage": random.randint(5, 45),
            "network_activity": random.randint(10, 50),
            "file_access_rate": random.randint(0, 7)
        }

# Detect anomalies
def detect_anomalies(values):
    anomalies = {}
    for k, (low, high) in baseline.items():
        v = values[k]
        if not (low <= v <= high):
            anomalies[k] = {
                "value": v,
                "expected_range": f"{low}-{high}"
            }
    return anomalies

# Respond to threat

def respond(anomalies):
    print(f"{Colors.FAIL}[⚠] Threat Detected! Containing...{Colors.ENDC}")
    time.sleep(1)
    for _ in range(3):
        print("[🛡️] Rolling back settings...")
        time.sleep(0.7)
    print(f"{Colors.OKGREEN}[✓] System healed and secured.\n{Colors.ENDC}")

# Visual style display

def display_state(values, anomalies):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{Colors.HEADER}--- CyberDNA Simulation --- [{timestamp}]{Colors.ENDC}\n")
    for key, value in values.items():
        color = Colors.FAIL if key in anomalies else Colors.OKGREEN
        print(f"{color}{key.replace('_', ' ').title()}: {value}{Colors.ENDC}")

    if anomalies:
        print(f"\n{Colors.WARNING}⚠ Anomalies Found:{Colors.ENDC}")
        print(json.dumps(anomalies, indent=4))
    else:
        print(f"\n{Colors.OKCYAN}✓ All systems normal. No threat detected.{Colors.ENDC}")

    print("\n-------------------------------\n")

# Run Simulation

def run_simulation(cycles=3):
    for i in range(cycles):
        clear_console()
        print(f"Cycle {i + 1} of {cycles}\n")
        values = simulate_behavior(i, cycles)
        anomalies = detect_anomalies(values)
        display_state(values, anomalies)
        if anomalies:
            respond(anomalies)
        else:
            time.sleep(2)

# Start
if __name__ == "__main__":
    run_simulation()

