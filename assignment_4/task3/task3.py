import os

# Create a pipe
r, w = os.pipe()

# Fork the process
pid = os.fork()

if pid > 0:
    # Parent Process
    os.close(r)  # Close reading end
    message = b"Hello from Parent Process!"
    os.write(w, message)
    os.close(w)  # Close writing end after sending
    os.wait()  # Wait for child to finish
else:
    # Child Process
    os.close(w)  # Close writing end
    message = os.read(r, 1024)  # Read from pipe
    print("Child received message:", message.decode())
    os.close(r)
