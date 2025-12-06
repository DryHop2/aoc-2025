from math import prod

PATH = "./inputs/day06.txt"


# with open(PATH, "r") as f:
#     lines = [line.split() for line in f]

# operands = [list(map(int, line)) for line in lines[:4]]
# ops = lines[4]


# result = 0

# for col, op in enumerate(ops):
#     a, b, c, d = (operands[row][col] for row in range(4))

#     if op == "*":
#         result += a * b * c * d
#     elif  op == "+":
#         result += a + b + c + d

# print(result)


def read_grid(path: str) -> list[list[str]]:
    with open(path) as f:
        lines = [line.rstrip("\n") for line in f]

    width = max(len(line) for line in lines)
    grid = [list(line.ljust(width)) for line in lines]
    return grid


def column_is_blank(grid: list[list[str]], c: int) -> bool:
    return all(row[c] == " " for row in grid)


def find_problems(grid: list[list[str]]) -> list[list[int]]:
    rows, cols = len(grid), len(grid[0])
    problems: list[list[int]] = []

    c = cols - 1
    while c >= 0:
        if column_is_blank(grid, c):
            c -= 1
            continue

        problem_cols: list[int] = []
        while c >= 0 and not column_is_blank(grid, c):
            problem_cols.append(c)
            c -= 1

        problems.append(problem_cols)

    return problems


def eval_problem(grid: list[list[str]], cols: list[int]) -> int:
    rows = len(grid)
    nums: list[int] = []
    op: str | None = None

    for c in cols:
        col_chars = [grid[r][c] for r in range(rows)]

        if col_chars[-1] in {"+", "*"}:
            op = col_chars[-1]

        digits = "".join(ch for ch in col_chars[:-1] if ch != " ")
        if digits:
            nums.append(int(digits))

    if op == "+":
        return sum(nums)
    elif op == "*":
        return prod(nums)
    else:
        raise ValueError("No operator found")
    

def total_math(path: str) -> int:
    grid = read_grid(path)
    problems = find_problems(grid)

    total = 0
    for cols in problems:
        total += eval_problem(grid, cols)
    
    return total


if __name__ == "__main__":
    result = total_math(PATH)
    print(result)