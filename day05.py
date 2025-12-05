PATH = "./inputs/day05.txt"


def parse_database(path: str) -> tuple[list[tuple[int, int]], list[int]]:
    with open(path) as f:
        lines = [line.strip() for line in f]

    blank_index = lines.index("")

    fresh_ranges: list[tuple[int, int]] = []
    for line in lines[:blank_index]:
        start, end = map(int, line.split("-"))
        fresh_ranges.append((start, end))

    available_ids = [int(x) for x in lines[blank_index + 1:]]

    return fresh_ranges, available_ids


def is_fresh(ingredient_id: int, ranges: list[tuple[int, int]]) -> bool:
    return any(lo <= ingredient_id <= hi for lo, hi in ranges)


def count_fresh_ingredients(path: str) -> int:
    fresh_ranges, available_ids = parse_database(path)
    return sum(1 for id_ in available_ids if is_fresh(id_, fresh_ranges))


if __name__ == "__main__":
    result = count_fresh_ingredients(PATH)
    print(result)