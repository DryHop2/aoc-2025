PATH = "./inputs/day04.txt"
DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
]


# def count_accessible(path: str) -> int:
#     with open(PATH, "r") as f:
#         grid = [line.rstrip("\n") for line in f]

#     rows = len(grid)
#     cols = len(grid[0])

#     directions = [
#         (-1, -1), (-1, 0), (-1, 1),
#         ( 0, -1),          ( 0, 1),
#         ( 1, -1), ( 1, 0), ( 1, 1),
#     ]

#     accessible = []

#     for r in range(rows):
#         for c in range(cols):
#             if grid[r][c] != "@":
#                 continue

#             neighbors = 0
#             for dr, dc in directions:
#                 rr, cc = r + dr, c + dc
#                 if 0 <= rr < rows and 0 <= cc < cols:
#                     if grid[rr][cc] == "@":
#                         neighbors += 1
#                         if neighbors == 4:
#                             break

#             if neighbors < 4:
#                 accessible.append((r, c))

#     return len(accessible)

def find_accessible(grid: list[list[str]]) -> list[tuple[int, int]]:
    rows = len(grid)
    cols = len(grid[0])
    accessible: list[tuple[int, int]] = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue

            neighbors = 0
            for dr, dc in DIRECTIONS:
                rr, cc = r + dr, c + dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    if grid[rr][cc] == "@":
                        neighbors += 1
                        if neighbors == 4:
                            break

            if neighbors < 4:
                accessible.append((r, c))

    return accessible


def total_remove(path: str) -> int:
    with open(path) as f:
        grid = [list(line.rstrip("\n")) for line in f]

    remove_total = 0

    while True:
        accessible = find_accessible(grid)
        if not accessible:
            break

        for r, c in accessible:
            grid[r][c] = "."

        remove_total += len(accessible)

    return remove_total


if __name__ == "__main__":
    print(total_remove(PATH))