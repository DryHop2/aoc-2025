PATH = "./inputs/day04.txt"


def count_accessible(path: str) -> int:
    with open(PATH, "r") as f:
        grid = [line.rstrip("\n") for line in f]

    rows = len(grid)
    cols = len(grid[0])

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
    ]

    accessible = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue

            neighbors = 0
            for dr, dc in directions:
                rr, cc = r + dr, c + dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    if grid[rr][cc] == "@":
                        neighbors += 1

            if neighbors < 4:
                accessible.append((r, c))

    return len(accessible)


if __name__ == "__main__":
    print(count_accessible(PATH))