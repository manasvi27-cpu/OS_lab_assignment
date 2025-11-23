# task2_sequential.py
# Simulation of Sequential File Allocation

# Input total number of blocks in memory
total_blocks = int(input("Enter total number of blocks: "))

# Initialize all blocks as free (0 = free, 1 = occupied)
block_status = [0] * total_blocks

# Input number of files
n = int(input("Enter number of files: "))

# Allocate each file
for i in range(n):
    start = int(input(f"Enter starting block for file {i+1}: "))
    length = int(input(f"Enter length of file {i+1}: "))
    
    allocated = True  # Flag to check if file can be allocated
    
    # Check if the requested blocks are free
    for j in range(start, start+length):
        if j >= total_blocks or block_status[j] == 1:
            allocated = False
            break
    
    # Allocate if possible
    if allocated:
        for j in range(start, start+length):
            block_status[j] = 1
        print(f"File {i+1} allocated from block {start} to {start+length-1}")
    else:
        print(f"File {i+1} cannot be allocated. Blocks are unavailable or exceed memory.")
