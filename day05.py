PATH = "./inputs/day05.txt"


# def parse_database(path: str) -> tuple[list[tuple[int, int]], list[int]]:
#     with open(path) as f:
#         lines = [line.strip() for line in f]

#     blank_index = lines.index("")

#     fresh_ranges: list[tuple[int, int]] = []
#     for line in lines[:blank_index]:
#         start, end = map(int, line.split("-"))
#         fresh_ranges.append((start, end))

#     available_ids = [int(x) for x in lines[blank_index + 1:]]

#     return fresh_ranges, available_ids


# def is_fresh(ingredient_id: int, ranges: list[tuple[int, int]]) -> bool:
#     return any(lo <= ingredient_id <= hi for lo, hi in ranges)


# def count_fresh_ingredients(path: str) -> int:
#     fresh_ranges, available_ids = parse_database(path)
#     return sum(1 for id_ in available_ids if is_fresh(id_, fresh_ranges))


def parse_fresh_ranges(path: str) -> list[tuple[int, int]]:
    with open(path) as f:
        lines = [line.strip() for line in f]

    blank_index = lines.index("")
    range_lines = lines[:blank_index]

    ranges: list[tuple[int, int]] = []
    for line in range_lines:
        lo, hi = map(int, line.split("-"))
        ranges.append((lo, hi))
    return ranges


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not ranges:
        return []
    
    ranges.sort(key=lambda r: (r[0], r[1]))
    merged: list[tuple[int, int]] = [ranges[0]]

    for lo, hi in ranges[1:]:
        cur_lo, cur_hi = merged[-1]

        if lo <= cur_hi:
            merged[-1] = (cur_lo, max(cur_hi, hi))
        else:
            merged.append((lo, hi))

    return merged


def count_fresh_ids(path: str) -> int:
    ranges = parse_fresh_ranges(path)
    merged = merge_ranges(ranges)

    total = 0
    for lo, hi in merged:
        total += hi - lo + 1
    
    return total


if __name__ == "__main__":
    result = count_fresh_ids(PATH)
    print(result)