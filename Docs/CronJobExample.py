"""
Certainly! In Python, you can set up cron jobs to run scripts at scheduled times. 
While traditional cron jobs are managed by the operating system's cron daemon, you can also use 
Python libraries to schedule tasks directly from within your Python application
"""
# save this as `my_script.py`
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='my_script.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def main():
    logging.info('Cron job executed')

if __name__ == "__main__":
    main()

"""
Ensure your script is executable. You can set the executable permission using

chmod +x my_script.py

crontab -e

0 3 * * * /usr/bin/python3 /path/to/my_script.py

Save and exit the editor. This line tells cron to run the Python script every day at 3 AM.
"""

# Example 2

"""
If you prefer to manage scheduling within your Python application, you can use libraries like schedule or APScheduler.

pip install schedule

python3 scheduler_script.py
"""

# save this as `scheduler_script.py`
import schedule
import time
import logging

# Configure logging
logging.basicConfig(filename='scheduler_script.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def job():
    logging.info('Scheduled task executed')

# Schedule the job
schedule.every().day.at("03:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)  # wait one minute


# Example 2 - Tuple Unpacking

def swap_three_numbers(a, b, c):
    return c, a, b

# Example usage
x, y, z = 1, 2, 3
print(f"Original values: x={x}, y={y}, z={z}")

x, y, z = swap_three_numbers(x, y, z)
print(f"Swapped values: x={x}, y={y}, z={z}")