customers = [[5, 2], [5, 4], [10, 3], [20, 1]]
#initial_time = 5
#wait1 = [5]

wait1 = [customers[0][0]]
for i in range(0,len(customers)):
    z = wait1[i] + customers[i][1]
    wait1.append(z)
wait1.pop(0)
#print(wait1)

wait_time = [0]
for i in range(0, len(customers)):
    if wait1[i]>customers[i][0]:
        z = wait1[i]-customers[i][0]
        wait_time.append(z)
    else:
        z = customers[i][1]
        wait_time.append(z)
wait_time.pop(0)
#print(wait_time)

avgtime = 0.00
for i in range(0,len(wait_time)):
    avgtime = avgtime + float(wait_time[i])
avgtime = avgtime / len(wait_time)
print(f"Average waiting time for each customer is {avgtime}")


