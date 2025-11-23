import os
import sys
import time

def create_children_with_command(n, command):
    children_pids = []

    for i in range(1, n + 1):
        pid = os.fork()
        
        if pid == 0:
            # In child
            print(f"[Child #{i}] PID: {os.getpid()}, PPID: {os.getppid()}")
            print(f"[Child #{i}] Executing command: {command}")
            time.sleep(0.5)  # Slight delay for readability

            # Use os.execvp to run the command
            # Example: command = ["ls", "-l"]
            os.execvp(command[0], command)
            os._exit(0)  # Should never reach here if execvp succeeds

        else:
            # In parent
            print(f"[Parent] Created child #{i} with PID {pid}")
            children_pids.append(pid)

    print("[Parent] Waiting for all children...")
    for _ in children_pids:
        os.wait()
    print("[Parent] All children finished.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 task2.py <number_of_children> <command> [args...]")
        sys.exit(1)

    n = int(sys.argv[1])
    command = sys.argv[2:]  # The rest of arguments are the command
    create_children_with_command(n, command)
