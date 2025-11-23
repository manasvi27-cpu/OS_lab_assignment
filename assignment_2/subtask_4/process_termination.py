import logging
import time
import multiprocessing

# Setup logger
logging.basicConfig(
    filename='subtask4_log.txt',   # Relevant log file for Sub-Task 4
    level=logging.INFO,
    format='%(asctime)s - %(processName)s - %(message)s'
)

# Function to simulate a process task
def system_process(task_name):
    logging.info(f"{task_name} started")
    time.sleep(2)  # Simulate task delay
    logging.info(f"{task_name} ended")

if __name__ == '__main__':
    logging.info("Sub-Task 4: Starting processes for termination verification")

    # Create two processes
    p1 = multiprocessing.Process(target=system_process, args=('Process-1',))
    p2 = multiprocessing.Process(target=system_process, args=('Process-2',))

    # Start processes
    p1.start()
    p2.start()

    # Wait for processes to complete (proper termination)
    p1.join()
    p2.join()

    # Log system shutdown
    logging.info("Sub-Task 4: System Shutdown completed")
