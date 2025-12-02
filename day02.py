with open("./inputs/day02.txt", "r") as f:
    line = f.read().strip()
    pids = line.split(",")

result = 0

for i in pids:
    pid_range = i.split("-")
    for n in range(int(pid_range[0]), int(pid_range[1]) + 1):
        if len(str(n)) % 2 != 0:
            continue
        midpoint = int(len(str(n)) / 2)
        if str(n)[:midpoint] == str(n)[midpoint:]:
            result += n

print(result)