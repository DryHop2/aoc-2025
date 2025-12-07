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

def read_grid(path: str) -> list[str]:
    with open(path) as f:
        lines = [line.rstrip("\n") for line in f]
    
    width = max(len(line) for line in lines)
    return [line.ljust(width) for line in lines]


def find_symbol(grid: list[str], symbol: str = "S") -> tuple[int, int]:
    for r, row in enumerate(grid):
        c = row.find(symbol)
        if c != -1:
            return r, c
    raise ValueError(f"Symbol {symbol!r} not found in grid")


def step_quantum_row(row: str, timelines: list[int]) -> list[int]:
    cols = len(row)
    next_timelines = [0] * cols

    for c, count in enumerate(timelines):
        if count == 0:
            continue
        cell = row[c]

        if cell == "." or cell == "S":
            next_timelines[c] += count
        elif cell == "^":
            if c > 0:
                next_timelines[c - 1] += count
            if c < cols - 1:
                next_timelines[c + 1] += count
        else:
            pass
    
    return next_timelines


def count_timelines(grid: list[str]) -> int:
    rows, cols = len(grid), len(grid[0])
    start_row, start_col = find_symbol(grid, "S")

    timelines = [0] * cols
    timelines[start_col] = 1

    for r in range(start_row + 1, rows):
        timelines = step_quantum_row(grid[r], timelines)

    return sum(timelines)


def main(path: str = PATH) -> None:
    grid = read_grid(path)
    total_timelines = count_timelines(grid)
    print(total_timelines)


if __name__ == "__main__":
    main()