import matplotlib.pyplot as plt
import subprocess

d = [0, 0, 0, 0, 0, 0]

def get_time(line):
    return float(line[line.index("user") + len("user") + 4 : -3])

def set_times(data):
    lines = str(data).split("sys")
    i = 0
    for line in lines[:-1]:
        d[i] = get_time(line)
        i += 1
                
set_times(subprocess.run(
    ["""
     #!/bin/bash
     time bash generate-dataset.sh plot_1000.txt 1000
     time bash generate-dataset.sh plot_100000.txt 100000
     time bash generate-dataset.sh plot_10000000.txt 10000000
     
     time bash sort-data.sh plot_1000.txt
     time bash sort-data.sh plot_100000.txt
     time bash sort-data.sh plot_10000000.txt
     """],
    shell=True,
    capture_output=True
).stderr)

print(" ".join(str(x) + "s" for x in d), sep="\n")

plt.plot(
    [1000, 100000, 10000000], 
    [d[0], d[1], d[2]], 
    label="gen"
)
plt.plot(
    [1000, 100000, 10000000], 
    [d[3], d[4], d[5]], 
    label="sort"
) 
plt.xlabel("Record number")
plt.ylabel("Time in seconds")
plt.legend()
plt.title("Data times")
plt.savefig("data_times.jpg")
plt.close()