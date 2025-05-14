import os
import shutil
import logging
import schedule
import time

# Set up logging
log_file = "backup_log.log"
logging.basicConfig(filename=log_file, level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Function to perform backup
def backup_files():
    try:
        # Define source and destination paths
        source = "/home/noh/Desktop/ML Tutorials/scripts/"
        backup_dir = "/home/noh/Desktop/ML Tutorials/backup/"
        # Create a unique destination path with timestamp
        destination = os.path.join(backup_dir, f"{os.path.basename(source)}_{time.strftime('%Y-%m-%d_%H-%M-%S')}")
        
        # Perform the backup (copying the folder)
        shutil.copytree(source, destination)
        
        # Log the success
        logging.info(f"Backup created successfully at {destination}")
        print(f"Backup created at {destination}")
    except Exception as e:
        # Log the error
        logging.error(f"Backup failed: {e}")
        print(f"Backup failed: {e}")

# Schedule the backup to run every 5 seconds
schedule.every(5).seconds.do(backup_files)

while True:
    schedule.run_pending()
    time.sleep(1)
