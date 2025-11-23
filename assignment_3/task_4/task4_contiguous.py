# task4_contiguous.py
# Simulation of Contiguous Memory Allocation: First-fit, Best-fit, Worst-fit

def allocate_memory(strategy):
    print(f"\n--- {strategy.capitalize()} Fit Memory Allocation ---")
    
    # Input memory partitions and process sizes
    partitions = list(map(int, input("Enter partition sizes (space-separated): ").split()))
    processes = list(map(int, input("Enter process sizes (space-separated): ").split()))
    
    allocation = [-1] * len(processes)  # Keep track of allocated partition for each process
    
    for i, psize in enumerate(processes):
        idx = -1  # Partition index for allocation
        
        if strategy == "first":
            # First-fit: allocate to the first partition large enough
            for j, part in enumerate(partitions):
                if part >= psize:
                    idx = j
                    break
        
        elif strategy == "best":
            # Best-fit: allocate to the smallest partition large enough
            best_fit = float("inf")
            for j, part in enumerate(partitions):
                if part >= psize and part < best_fit:
                    best_fit = part
                    idx = j
        
        elif strategy == "worst":
            # Worst-fit: allocate to the largest partition available
            worst_fit = -1
            for j, part in enumerate(partitions):
                if part >= psize and part > worst_fit:
                    worst_fit = part
                    idx = j
        
        # Allocate memory if a suitable partition is found
        if idx != -1:
            allocation[i] = idx
            partitions[idx] -= psize
    
    # Display allocation results
    for i, a in enumerate(allocation):
        if a != -1:
            print(f"Process {i+1} allocated in Partition {a+1}")
        else:
            print(f"Process {i+1} cannot be allocated")

# Main Program
if __name__ == "__main__":
    allocate_memory("first")
    allocate_memory("best")
    allocate_memory("worst")

