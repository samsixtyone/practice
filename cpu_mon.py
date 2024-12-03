import subprocess
import time
import datetime

# Function to get CPU usage using vmstat
def get_cpu_usage():
    # Run the vmstat command and get the output
    result = subprocess.run(['vmstat', '1', '2'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    # Extract the CPU idle value from the output (assuming it's the 15th value in the second line)
    lines = output.splitlines()
    cpu_idle = int(lines[2].split()[15])  # Idle CPU percentage
    cpu_usage = 100 - cpu_idle  # Calculate CPU usage
    return cpu_usage

# Function to alert if CPU usage is 100% for 2 hours
def monitor_cpu_usage():
    alert_trigger_time = None

    while True:
        cpu_usage = get_cpu_usage()
        current_time = datetime.datetime.now()

        if cpu_usage == 100:
            # If CPU usage is 100%, record the time
            if alert_trigger_time is None:
                alert_trigger_time = current_time
                print(f"High CPU detected at {current_time}")
            elif (current_time - alert_trigger_time).total_seconds() >= 2 * 60 * 60:
                # If 2 hours have passed since the first detection, trigger the alert
                print(f"ALERT: CPU usage has been at 100% for 2 hours as of {current_time}")
                break
        else:
            # Reset the timer if CPU is not at 100%
            alert_trigger_time = None
        
        time.sleep(60)  # Check every minute

if __name__ == '__main__':
    monitor_cpu_usage()
