PATH = "./inputs/day06.txt"


with open(PATH, "r") as f:
    lines = [list(line.split()) for line in f]

operands = [list(map(int, line)) for line in lines[:4]]
ops = lines[4]


result = 0

for col, op in enumerate(ops):
    a, b, c, d = (operands[row][col] for row in range(4))

    if op == "*":
        result += a * b * c * d
    elif  op == "+":
        result += a + b + c + d

print(result)