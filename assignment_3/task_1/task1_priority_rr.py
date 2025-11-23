# task1_priority_rr.py
# Simulation of CPU Scheduling: Priority and Round Robin

# Function for Priority Scheduling
def priority_scheduling(processes):
    print("Priority Scheduling:\n")
    print("PID\tBT\tPriority\tWT\tTAT")
    
    # Sort processes by priority (lower number = higher priority)
    processes.sort(key=lambda x: x[2])
    
    wt = 0  # Waiting time
    total_wt = 0
    total_tt = 0
    
    for pid, bt, pr in processes:
        tat = wt + bt  # Turnaround Time
        print(f"{pid}\t{bt}\t{pr}\t\t{wt}\t{tat}")
        total_wt += wt
        total_tt += tat
        wt += bt  # Update waiting time
    
    print(f"\nAverage Waiting Time: {total_wt / len(processes):.2f}")
    print(f"Average Turnaround Time: {total_tt / len(processes):.2f}")
    print("-"*50)

# Function for Round Robin Scheduling
def round_robin_scheduling(processes, quantum):
    print(f"\nRound Robin Scheduling (Quantum = {quantum}):\n")
    print("PID\tBT\tWT\tTAT")
    
    n = len(processes)
    remaining_bt = [bt for _, bt, _ in processes]
    wt = [0]*n
    tat = [0]*n
    time_elapsed = 0
    
    while True:
        done = True
        for i in range(n):
            if remaining_bt[i] > 0:
                done = False
                if remaining_bt[i] > quantum:
                    time_elapsed += quantum
                    remaining_bt[i] -= quantum
                else:
                    time_elapsed += remaining_bt[i]
                    wt[i] = time_elapsed - processes[i][1]
                    remaining_bt[i] = 0
        if done:
            break
    
    for i in range(n):
        tat[i] = processes[i][1] + wt[i]
        print(f"{processes[i][0]}\t{processes[i][1]}\t{wt[i]}\t{tat[i]}")
    
    print(f"\nAverage Waiting Time: {sum(wt)/n:.2f}")
    print(f"Average Turnaround Time: {sum(tat)/n:.2f}")

# Main program
if __name__ == "__main__":
    processes = []
    n = int(input("Enter number of processes: "))
    
    for i in range(n):
        bt = int(input(f"Enter Burst Time for P{i+1}: "))
        pr = int(input(f"Enter Priority (lower number = higher priority) for P{i+1}: "))
        processes.append((i+1, bt, pr))
    
    priority_scheduling(processes.copy())
    
    quantum = int(input("Enter Time Quantum for Round Robin: "))
    round_robin_scheduling(processes.copy(), quantum)

