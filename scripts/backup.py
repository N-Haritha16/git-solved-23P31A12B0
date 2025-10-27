import os
import shutil
import datetime

def backup_files(source, destination):
    """Creates a timestamped backup of the source directory."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_folder = os.path.join(destination, f"backup-{timestamp}")
    try:
        shutil.copytree(source, backup_folder)
        print(f"✅ Backup created successfully at: {backup_folder}")
    except Exception as e:
        print(f"❌ Backup failed: {e}")

if __name__ == "__main__":
    source_dir = "./config"
    destination_dir = "./backups"
    os.makedirs(destination_dir, exist_ok=True)
    backup_files(source_dir, destination_dir)
