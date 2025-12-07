PATH = "./inputs/day07.txt"


with open(PATH, "r") as f:
    lines = [line.rstrip("\n") for line in f]

grid = [list(row) for row in lines]

rows = len(grid)
cols = len(grid[0])

start_row = 0
start_col = grid[0].index("S")

beams = {start_col}
splits = 0

for r in range(start_row + 1, rows):
    new_beams = set()

    for c in beams:
        ch = grid[r][c]

        if ch == ".":
            new_beams.add(c)
        elif ch == "^":
            if c > 0:
                new_beams.add(c - 1)
            if c < cols - 1:
                new_beams.add(c + 1)
            splits += 1

    beams = new_beams

beams_count = len(beams)
print(beams_count)
print(splits)