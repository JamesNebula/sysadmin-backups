import shutil
import socket
from datetime import datetime
import os

def check_disk_space(path='/', warning_threshold=80):
    # Check disk usage. Alert if usage > warning_threshold (%)
    total, used, free = shutil.disk_usage(path)
    usage_percent = (used / total) * 100
    
    hostname = socket.gethostname()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log_message(f"🖥️  Host: {hostname}")
    log_message(f"📅 Time: {now}")
    log_message(f"💽 Disk Usage: {usage_percent:.1f}% of {total // (2**30)} GB")
    
    if usage_percent > warning_threshold:
        log_message(f"⚠️  WARNING: Disk usage is {usage_percent:.1f}% — clean up space!")
        return False
    else:
        log_message(f"✅ OK: Disk usage is healthy.")
        return True

def log_message(message, log_file="disk_monitor.log"):
    with open(log_file, 'a') as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")
        
check_disk_space("/Users/jamescawthray/Desktop")

# Check specific path (e.g., where LiDAR data lives)
# check_disk_space("/Users/jamescawthray/Desktop")