PATH = "./inputs/day05.txt"


fresh_ranges = []
available = []

with open(PATH, "r") as f:
    lines = [line.strip() for line in f]

blank = lines.index("")
range_lines = lines[:blank]
available_lines = lines[blank + 1:]

for item in range_lines:
    lo, hi = item.split("-")
    fresh_ranges.append((int(lo), int(hi)))

available = [int(x) for x in available_lines]


def is_fresh(id_: int, ranges: list[tuple[int, int]]) -> bool:
    for lo, hi in ranges:
        if lo <= id_ <= hi:
            return True
    return False


result = sum(1 for ing in available if is_fresh(ing, fresh_ranges))

print(result)