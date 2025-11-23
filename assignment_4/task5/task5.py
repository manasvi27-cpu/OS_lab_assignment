# CPU Scheduling Algorithms - FCFS, SJF, Priority, Round Robin

def fcfs(processes):
    print("\n===== FCFS Scheduling =====")
    wt = [0] * len(processes)
    tat = [0] * len(processes)

    for i in range(1, len(processes)):
        wt[i] = processes[i-1][1] + wt[i-1]
    
    for i in range(len(processes)):
        tat[i] = wt[i] + processes[i][1]

    print("Process\tBT\tWT\tTAT")
    for i in range(len(processes)):
        print(f"{processes[i][0]}\t{processes[i][1]}\t{wt[i]}\t{tat[i]}")


def sjf(processes):
    print("\n===== SJF Scheduling =====")
    sorted_processes = sorted(processes, key=lambda x: x[1])
    fcfs(sorted_processes)


def priority_scheduling(processes):
    print("\n===== Priority Scheduling =====")
    sorted_processes = sorted(processes, key=lambda x: x[2])
    fcfs(sorted_processes)


def round_robin(processes, quantum):
    print("\n===== Round Robin Scheduling =====")
    bt = [proc[1] for proc in processes]
    wt = [0] * len(processes)
    rem_bt = bt.copy()
    t = 0

    while True:
        done = True

        for i in range(len(processes)):
            if rem_bt[i] > 0:
                done = False

                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t += rem_bt[i]
                    wt[i] = t - bt[i]
                    rem_bt[i] = 0

        if done:
            break

    tat = [bt[i] + wt[i] for i in range(len(processes))]

    print("Process\tBT\tWT\tTAT")
    for i in range(len(processes)):
        print(f"{processes[i][0]}\t{bt[i]}\t{wt[i]}\t{tat[i]}")


# SAMPLE PROCESS LIST: (PID, Burst Time, Priority)
processes = [
    ("P1", 6, 2),
    ("P2", 8, 1),
    ("P3", 7, 3),
    ("P4", 3, 2)
]

# Run Algorithms
fcfs(processes)
sjf(processes)
priority_scheduling(processes)
round_robin(processes, quantum=3)

