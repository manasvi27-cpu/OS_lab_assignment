# task3_indexed.py
# Simulation of Indexed File Allocation

# Input total number of memory blocks
total_blocks = int(input("Enter total number of blocks: "))

# Initialize all blocks as free (0 = free, 1 = allocated)
block_status = [0] * total_blocks

# Input number of files
n = int(input("Enter number of files: "))

for i in range(n):
    # Input index block for file
    index = int(input(f"\nEnter index block for file {i+1}: "))
    
    # Check if index block is already allocated
    if block_status[index] == 1:
        print("Index block already allocated. File cannot be allocated.")
        continue
    
    # Input number of data blocks and their numbers
    count = int(input("Enter number of data blocks for this file: "))
    data_blocks = list(map(int, input("Enter block numbers separated by space: ").split()))
    
    # Check for invalid input or already allocated blocks
    if len(data_blocks) != count:
        print("Error: Number of data blocks entered does not match count.")
        continue
    if any(block_status[blk] == 1 for blk in data_blocks):
        print("Error: One or more data blocks are already allocated.")
        continue
    
    # Allocate index block and data blocks
    block_status[index] = 1
    for blk in data_blocks:
        block_status[blk] = 1
    
    print(f"File {i+1} allocated with index block {index} -> {data_blocks}")
