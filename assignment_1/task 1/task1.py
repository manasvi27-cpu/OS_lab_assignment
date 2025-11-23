import os
import sys
import time

def create_children(n):
    children_pids = []

    for i in range(1, n + 1):
        pid = os.fork()
        
        if pid == 0:
            # In child
            print(f"I am child #{i}")
            print(f"My PID: {os.getpid()}")
            print(f"My Parent PID: {os.getppid()}")
            print("Custom message: Hello from child!")
            time.sleep(1)
            os._exit(0)
        else:
            # In parent
            print(f"Parent created child #{i} with PID {pid}")
            children_pids.append(pid)

    print("Parent waiting for children...")
    for _ in children_pids:
        os.wait()
    print("Parent finished waiting.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 task1.py <number_of_children>")
        sys.exit(1)

    n = int(sys.argv[1])
    create_children(n)
