import os
import time

print("=== TASK 3: Zombie and Orphan Processes ===\n")

# ------------------------
# Part 1: Zombie Process
# ------------------------
print("--- Zombie Process Example ---")
pid = os.fork()

if pid == 0:
    # Child process
    print(f"[Zombie Child] PID: {os.getpid()} - finishing quickly, will become zombie")
    time.sleep(5)  # Child “finishes” but parent has not waited yet
    os._exit(0)
else:
    # Parent process does NOT wait immediately
    print(f"[Parent] PID: {os.getpid()} created child PID: {pid} (will not wait yet)")
    
    # Show zombies automatically
    print("\n[Parent] Checking for zombie processes (defunct) while child is finished:")
    time.sleep(6)  # Wait for child to finish and become zombie
    os.system("ps -el | grep defunct")
    
    # Now clean up child
    os.wait()
    print("[Parent] Finished waiting for zombie child.\n")

# ------------------------
# Part 2: Orphan Process
# ------------------------
print("--- Orphan Process Example ---")
pid = os.fork()

if pid == 0:
    # Child process
    print(f"[Orphan Child] PID: {os.getpid()} - My parent PID: {os.getppid()}")
    time.sleep(5)  # simulate long work
    print(f"[Orphan Child] PID: {os.getpid()} - My new parent PID (should be 1): {os.getppid()}")
    os._exit(0)
else:
    # Parent exits immediately, making child an orphan
    print(f"[Parent] PID: {os.getpid()} is exiting immediately to create orphan child")
    os._exit(0)
