import os 
import shutil
from datetime import datetime
from pathlib import Path
import platform
import socket

def backup_files(src_folder, backup_root='backups'):
    print(f"🌿 Running SysAdmin Buddy on: {platform.system()} {platform.release()}")
    print(f"💻 Host: {socket.gethostname()}")
    
    src_path = Path(src_folder).expanduser()
    if not src_path.exists():
        print(f"❌ Source folder not found: {src_path}")
        return
    
    backup_root_path = Path(backup_root)
    today = datetime.now().strftime("%Y-%m-%d_%H-%M")
    backup_path = backup_root_path / today
    backup_path.mkdir(parents=True, exist_ok=True)
    
    copied = 0
    for file in src_path.iterdir():
        if file.is_file():
            shutil.copy(file, backup_path / file.name)
            print(f"✅ Backed up: {file.name}")
            copied += 1
    
    #log system info
    log_path = backup_path / "backup.log"
    with open(log_path, 'w') as log:
        log.write(f"Backup completed: {datetime.now()}\n")
        log.write(f"System: {platform.system()} {platform.release()}\n")
        log.write(f"Machine: {platform.machine()}\n")
        log.write(f"Hostname: {socket.gethostname()}\n")
        log.write(f"Python: {platform.python_version()}\n")
        log.write(f"Files backed up: {copied}\n")

    print(f"📊 Backup log saved to: {log_path}")
    print(f"🎉 {copied} files backed up successfully!")
    
#Backup desktop
backup_files("~/Desktop")