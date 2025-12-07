PATH = "./inputs/day07.txt"


# with open(PATH, "r") as f:
#     lines = [line.rstrip("\n") for line in f]

# grid = [list(row) for row in lines]

# rows = len(grid)
# cols = len(grid[0])

# start_row = 0
# start_col = grid[0].index("S")

# beams = {start_col}
# splits = 0

# for r in range(start_row + 1, rows):
#     new_beams = set()

#     for c in beams:
#         ch = grid[r][c]

#         if ch == ".":
#             new_beams.add(c)
#         elif ch == "^":
#             if c > 0:
#                 new_beams.add(c - 1)
#             if c < cols - 1:
#                 new_beams.add(c + 1)
#             splits += 1

#     beams = new_beams

# beams_count = len(beams)
# print(beams_count)
# print(splits)

with open(PATH) as f:
    grid = [line.rstrip("\n") for line in f]

rows = len(grid)
cols = len(grid[0])

start_row = 0
start_col = grid[start_row].index("S")

timelines = [0] * cols
timelines[start_col] = 1

for r in range(start_row + 1, rows):
    new_timelines = [0] * cols

    for c in range(cols):
        count = timelines[c]
        if count == 0:
            continue

        cell = grid[r][c]

        if cell == ".":
            new_timelines[c] += count
        elif cell == "^":
            if c > 0:
                new_timelines[c - 1] += count
            if c < cols - 1:
                new_timelines[c + 1] += count
        elif cell == "S":
            new_timelines[c] += count

    timelines = new_timelines

total_timelines = sum(timelines)
print(total_timelines)