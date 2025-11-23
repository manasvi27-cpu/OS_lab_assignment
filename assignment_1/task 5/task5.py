import os
import time

print("=== TASK 5: Process Prioritization ===\n")

# Number of child processes
num_children = 3

# Different nice values for each child
nice_values = [0, 5, 10]  # 0 = default, higher = lower priority

child_pids = []

def cpu_intensive_task():
    """Simple CPU-intensive task: sum of numbers"""
    total = 0
    for i in range(1, 10000000):
        total += i
    print(f"[Child PID {os.getpid()}] Finished CPU task.")

# Fork child processes
for i in range(num_children):
    pid = os.fork()
    if pid == 0:
        # Child process
        os.nice(nice_values[i])  # Set priority
        print(f"[Child PID {os.getpid()}] Starting with nice value {nice_values[i]}")
        start_time = time.time()
        cpu_intensive_task()
        end_time = time.time()
        print(f"[Child PID {os.getpid()}] Execution time: {end_time - start_time:.2f} seconds")
        os._exit(0)
    else:
        # Parent stores child PID
        child_pids.append(pid)

# Parent waits for all children
for pid in child_pids:
    os.waitpid(pid, 0)

print("\n[Parent] All child processes finished.")
