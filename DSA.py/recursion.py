bt = [4, 3, 7, 1, 2]

bt.sort()

waiting_time = 0
total_waiting_time = 0

for i in range(len(bt)):
    total_waiting_time += waiting_time
    waiting_time += bt[i]

avg_waiting_time = total_waiting_time // len(bt)

print(avg_waiting_time)