import os
import time

print("=== TASK 3: Zombie and Orphan Processes ===\n")

# ------------------------
# Part 1: Zombie Process
# ------------------------
print("--- Zombie Process Example ---")
pid = os.fork()

if pid == 0:
    # Child process exits immediately to become zombie
    print(f"[Zombie Child] PID: {os.getpid()} - finishing quickly, will become zombie")
    os._exit(0)
else:
    # Parent does not wait immediately
    print(f"[Parent] PID: {os.getpid()} created child PID: {pid} (will not wait yet)")
    time.sleep(5)  # give child time to become zombie

    print("\n[Parent] Checking for zombie processes (defunct) while child is finished:")
    os.system("ps -el | grep defunct")  # show zombies

    os.wait()  # now clean up child
    print("[Parent] Finished waiting for zombie child.\n")

# ------------------------
# Part 2: Orphan Process
# ------------------------
print("--- Orphan Process Example ---")
pid = os.fork()

if pid == 0:
    # Child sleeps to allow parent to exit first
    time.sleep(5)
    print(f"[Orphan Child] PID: {os.getpid()} - My new parent PID (should be 1): {os.getppid()}")
    os._exit(0)
else:
    # Parent exits immediately to create orphan
    print(f"[Parent] PID: {os.getpid()} is exiting immediately to create orphan child")
    os._exit(0)

