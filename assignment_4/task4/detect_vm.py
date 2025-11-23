import subprocess

def check_vm():
    try:
        result = subprocess.check_output("systemd-detect-virt", shell=True).decode().strip()
        if result == "none":
            print("This system is running on Bare Metal (Not a VM).")
        else:
            print(f"This system is running inside a Virtual Machine: {result}")
    except Exception as e:
        print("Could not detect virtualization:", e)

check_vm()
