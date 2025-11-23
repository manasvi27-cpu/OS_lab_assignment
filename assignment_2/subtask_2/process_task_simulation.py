import logging
import time

# Setup logger
logging.basicConfig(
    filename='subtask2_log.txt',   # Relevant log file for Sub-Task 2
    level=logging.INFO,
    format='%(asctime)s - %(processName)s - %(message)s'
)

# Log system startup for Sub-Task 2
logging.info("Sub-Task 2: System process task simulation initialized.")

# Function to simulate a process task
def system_process(task_name):
    logging.info(f"{task_name} started")
    time.sleep(2)  # Simulate task delay
    logging.info(f"{task_name} ended")

# Example usage
system_process("Process A")
