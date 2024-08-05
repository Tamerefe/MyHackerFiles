import time
import sys
import random

# ANSI escape codes for colors
COLOR_GREEN = "\033[92m"  # Green
COLOR_RED = "\033[91m"    # Red
COLOR_BLUE = "\033[94m"   # Blue
COLOR_YELLOW = "\033[93m" # Yellow
COLOR_MAGENTA = "\033[95m" # Magenta
COLOR_RESET = "\033[0m"   # Reset to default

def colorize_text(text):
    """Colorizes the text based on its type."""
    if "[INFO]" in text:
        return COLOR_BLUE + text + COLOR_RESET
    elif "[ALERT]" in text or "[INPUT]" in text:
        return COLOR_YELLOW + text + COLOR_RESET
    elif "[DEBUG]" in text:
        return COLOR_RED + text + COLOR_RESET
    elif "[SECURITY]" in text or "[UPDATE]" in text or "[SUCCESS]" in text:
        return COLOR_GREEN + text + COLOR_RESET
    elif "[QUIT]" in text:
        return COLOR_MAGENTA + text + COLOR_RESET
    return text

def slow_print(text, delay=0.004, pause_duration=None):
    """Prints the text slowly on the screen and adds a pause at specific points."""
    text = colorize_text(text)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
        
    if pause_duration:
        time.sleep(pause_duration)  # Adds a specific pause duration

    print()  # Move to a new line

def process_logs(logs):
    for index, log in enumerate(logs, start=1):
        # Add a 2-second pause at a randomly chosen log
        pause_at = random.randint(1, len(logs))
        pause_duration = 2 if index == pause_at else 0.004

        # Prompt for the user name after the fifth log entry
        if index == 5:
            time.sleep(0.02)
            user_name = input(COLOR_YELLOW + "[INPUT] Please enter 'target' user name: " + COLOR_RESET)
            slow_print(COLOR_YELLOW + f"[INPUT] Target Name '{user_name}'" + COLOR_RESET, delay=0.02)
            time.sleep(1)  # Short pause before continuing with logs

        # Prompt for additional action after the 80th log entry
        if index == 80:
            action = input(COLOR_YELLOW + "Do you want to perform another action? (y/n): " + COLOR_RESET).strip().lower()
            if action == 'y':
                return True  # Restart the process

        slow_print(log, delay=0.004, pause_duration=pause_duration)

    return False  # Continue to the end of the logs

# Print welcome message
slow_print(COLOR_GREEN + "Welcome to the **Target** Finder application...\n" + COLOR_RESET, delay=0.04)
time.sleep(1)  # Short pause before the next input

# Ask for the application name
time.sleep(0.5)
application_name = input(COLOR_YELLOW + "[INPUT] Please enter the application name: " + COLOR_RESET)
slow_print(COLOR_YELLOW + f"[INPUT] Checking Application Name **{application_name}**" + COLOR_RESET, delay=0.02)
time.sleep(1)  # Short pause before the next input

# Random text effect logs
logs = [
    "[INFO] System boot initiated...",
    "[INFO] Loading kernel modules...",
    "[DEBUG] Network interface eth0 detected",
    "[DEBUG] Initializing network protocols...",
    "[INFO] Performing security check...",
    "[SECURITY] User authentication successful",
    "[INFO] System initialization complete",
    "[INFO] Scanning for vulnerabilities...",
    "[UPDATE] Connecting to target server...",
    "[UPDATE] Exploit script initiated",
    "[UPDATE] Bypassing firewall protections...",
    "[UPDATE] Exploit successful, gaining root access",
    "[SUCCESS] Root access acquired",
    "[SUCCESS] Extracting sensitive files...",
    "[SUCCESS] Data transfer in progress",
    "[INFO] Monitoring network traffic...",
    "[INFO] Analyzing data packets...",
    "[DEBUG] Packet loss detected: 0.02%",
    "[INFO] Updating intrusion detection system...",
    "[ALERT] Unauthorized access attempt detected",
    "[WARNING] Potential security breach identified",
    "[INFO] Conducting security audit...",
    "[UPDATE] Verifying system integrity...",
    "[DEBUG] Memory leak detected in module X",
    "[INFO] Patching vulnerability in module X...",
    "[UPDATE] Firewall rules updated",
    "[SUCCESS] Firewall bypassed",
    "[SUCCESS] Secure shell (SSH) connection established",
    "[INFO] Accessing remote database...",
    "[UPDATE] Retrieving sensitive data",
    "[UPDATE] Decrypting files...",
    "[ALERT] Data encryption keys exposed",
    "[ERROR] Encryption failed: Key mismatch",
    "[INFO] Initiating fallback protocols...",
    "[DEBUG] Re-establishing secure connection...",
    "[UPDATE] Applying security patches",
    "[SUCCESS] Security patches applied",
    "[INFO] Synchronizing system clocks...",
    "[INFO] Monitoring server load...",
    "[DEBUG] High CPU usage detected: 87%",
    "[INFO] Optimizing server performance...",
    "[UPDATE] Increasing memory allocation",
    "[INFO] Scanning for malware...",
    "[ALERT] Suspicious activity detected: Trojan",
    "[ERROR] Malware removal failed: Access denied",
    "[INFO] Restarting affected services...",
    "[UPDATE] Updating virus definitions",
    "[INFO] Performing backup of critical data...",
    "[SUCCESS] Backup completed successfully",
    "[INFO] Verifying backup integrity...",
    "[INFO] Checking for system updates...",
    "[UPDATE] Downloading security updates",
    "[INFO] Applying updates...",
    "[SUCCESS] System updated to version 5.1.3",
    "[DEBUG] Network traffic analysis complete",
    "[INFO] System performance: Optimal",
    "[WARNING] High number of failed login attempts",
    "[ALERT] Possible brute force attack",
    "[INFO] Blocking IP addresses...",
    "[UPDATE] IP addresses blocked: 192.168.1.1, 192.168.1.2",
    "[SUCCESS] IP blocking successful",
    "[INFO] Performing system health check...",
    "[INFO] Generating system report...",
    "[INFO] Report generation complete",
    "[DEBUG] System logs reviewed",
    "[INFO] Archiving old logs...",
    "[SUCCESS] Logs archived successfully",
    "[INFO] Cleaning up temporary files...",
    "[INFO] File cleanup complete",
    "[UPDATE] Rebooting system for updates",
    "[INFO] System reboot initiated...",
    "[INFO] Rebooting in 10 seconds",
    "[DEBUG] Monitoring reboot progress...",
    "[INFO] Reboot successful",
    "[INFO] System back online",
    "[DEBUG] Checking system status...",
    "[INFO] All services operational",
    "[INFO] Performing final security check...",
    "[SUCCESS] No issues detected",
    "[INFO] System operational and secure",
    "[INFO] Closing security logs...",
    "[SUCCESS] Security logs closed",
    "[QUIT] Logging out...",
    "[QUIT] User session terminated",
    "[QUIT] System shutdown initiated...",
    "[QUIT] Shutting down in 10 seconds"
]

# Process the logs
while process_logs(logs):
    # Restart the logs from the beginning if the user chose to perform another action
    slow_print(COLOR_GREEN + "\nRestarting the process...\n" + COLOR_RESET, delay=0.004)
    time.sleep(1)  # Short pause before restarting
