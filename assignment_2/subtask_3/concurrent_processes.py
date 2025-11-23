import logging
import time
import multiprocessing

# Setup logger
logging.basicConfig(
    filename='subtask3_log.txt',   # Relevant log file for Sub-Task 3
    level=logging.INFO,
    format='%(asctime)s - %(processName)s - %(message)s'
)

# Function to simulate a process task
def system_process(task_name):
    logging.info(f"{task_name} started")
    time.sleep(2)  # Simulate task delay
    logging.info(f"{task_name} ended")

# Run processes concurrently
if __name__ == '__main__':
    logging.info("Sub-Task 3: Starting concurrent processes")
    
    # Create two processes
    p1 = multiprocessing.Process(target=system_process, args=('Process-1',))
    p2 = multiprocessing.Process(target=system_process, args=('Process-2',))
    
    # Start processes
    p1.start()
    p2.start()
    
    # Wait for processes to complete
    p1.join()
    p2.join()
    
    logging.info("Sub-Task 3: All processes completed")

