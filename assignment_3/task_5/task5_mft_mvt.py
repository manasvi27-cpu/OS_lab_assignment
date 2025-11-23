# task5_mft_mvt.py
# Simulation of Memory Management: MFT (Fixed) and MVT (Variable)

def MFT():
    print("\n--- MFT (Fixed Partitioning) Simulation ---")
    
    # Input total memory size and fixed partition size
    mem_size = int(input("Enter total memory size: "))
    part_size = int(input("Enter partition size: "))
    
    partitions = mem_size // part_size
    print(f"Memory divided into {partitions} partitions of size {part_size}")
    
    # Input number of processes
    n = int(input("Enter number of processes: "))
    
    for i in range(n):
        psize = int(input(f"Enter size of Process {i+1}: "))
        if psize <= part_size:
            print(f"Process {i+1} allocated to a partition.")
        else:
            print(f"Process {i+1} too large for fixed partition.")

def MVT():
    print("\n--- MVT (Variable Partitioning) Simulation ---")
    
    mem_size = int(input("Enter total memory size: "))
    n = int(input("Enter number of processes: "))
    
    for i in range(n):
        psize = int(input(f"Enter size of Process {i+1}: "))
        if psize <= mem_size:
            print(f"Process {i+1} allocated. Remaining memory: {mem_size - psize}")
            mem_size -= psize
        else:
            print(f"Process {i+1} cannot be allocated. Not enough memory.")

# Main Program
if __name__ == "__main__":
    print("MFT Simulation:")
    MFT()
    
    print("\nMVT Simulation:")
    MVT()

