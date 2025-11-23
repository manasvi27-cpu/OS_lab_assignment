import os

print("=== TASK 4: Inspect Process Info from /proc ===\n")

# Take PID as input
pid = input("Enter PID of process to inspect: ").strip()

proc_status_path = f"/proc/{pid}/status"
proc_exe_path = f"/proc/{pid}/exe"
proc_fd_path = f"/proc/{pid}/fd"

# ------------------------
# Read /proc/[pid]/status
# ------------------------
try:
    with open(proc_status_path, "r") as f:
        status_lines = f.readlines()
        print("--- Process Status (/proc/[pid]/status) ---")
        for line in status_lines:
            if line.startswith(("Name:", "State:", "VmSize:")):
                print(line.strip())
except FileNotFoundError:
    print(f"Error: Process {pid} not found.")

# ------------------------
# Executable path
# ------------------------
try:
    exe_path = os.readlink(proc_exe_path)
    print("\n--- Executable Path (/proc/[pid]/exe) ---")
    print(exe_path)
except FileNotFoundError:
    print(f"Error: Executable for PID {pid} not found.")
except PermissionError:
    print(f"Error: Permission denied for reading /proc/{pid}/exe.")

# ------------------------
# Open file descriptors
# ------------------------
try:
    fds = os.listdir(proc_fd_path)
    print("\n--- Open File Descriptors (/proc/[pid]/fd) ---")
    if fds:
        for fd in fds:
            print(f"FD {fd} -> {os.readlink(os.path.join(proc_fd_path, fd))}")
    else:
        print("No open file descriptors.")
except FileNotFoundError:
    print(f"Error: /proc/{pid}/fd not found.")
except PermissionError:
    print(f"Error: Permission denied for reading /proc/{pid}/fd.")
