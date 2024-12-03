import shutil
import time
import os


def check_disk_usage():
    partitions = shutil.disk_usage("/")
    total,used,free = partitions.total, partitions.used, partitions.free
    usage_percentage = (used/total)*100
    return usage_percentage

def monitor_disk_usage():
    while True:
        usage = check_disk_usage()
        if usage > 95:
            print(f"Alert Disk Usage at {usage:.2f}%")
            with open("disk_alert.log", "a") as log_file:
                log_file.write(f"Alert disk usage at {usage:.2f}% - {time.ctime()}\n")
        else:
            print (f"Disk usage is Normal: {usage:.2f}%  -·{time.ctime()}\n")
        
        time.sleep(60)

if __name__ == "__main__":
    monitor_disk_usage()
