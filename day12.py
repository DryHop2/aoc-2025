from math import prod


PATH = "./inputs/day12.txt"


def parse(path: str):
    text = open(path).read().strip()
    blocks = text.split("\n\n")

    shape_blocks = blocks[:-1]
    region_blocks = blocks[-1]
    shape_areas = [b.count("#") for b in shape_blocks]
    regions = []

    for line in region_blocks.splitlines():
        if not line.strip():
            continue
        parts = line.replace("x", " ").replace(":", " ").split()
        w, h = map(int, parts[:2])
        counts = list(map(int, parts[2:]))
        regions.append((w, h, counts))

    return shape_areas, regions


def part1(path: str) -> int:
    shape_areas, regions = parse(path)

    valid = 0
    for w, h, counts in regions:
        board_area = w * h
        present_area = sum(c * shape_areas[i] for i, c in enumerate(counts))
        if present_area <= board_area:
            valid += 1

    return valid


if __name__ == "__main__":
    print(part1(PATH))
    