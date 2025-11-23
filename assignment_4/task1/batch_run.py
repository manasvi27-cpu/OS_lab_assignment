import subprocess

scripts = ['script1.py', 'script2.py', 'script3.py']

print("\n🔵 Batch Processing Started...\n")

for script in scripts:
    print(f"➡️ Executing {script}...")
    subprocess.call(['python3', script])

print("\n🟢 Batch Processing Completed!\n")

