DIAL_SIZE = 100
DIAL_START = 50
PATH = "./inputs/day01.txt"


def count_zero_hits(position: int, direction: str, distance: int, dial_size: int = 100) -> int:
    if distance <= 0:
        return 0
    
    if direction == "R":
        first = dial_size if position == 0 else dial_size - position
    elif direction == "L":
        first = dial_size if position == 0 else position
    else:
        raise ValueError(f"Unknown direction: {direction!r}")

    if distance < first:
        return 0
    
    return 1 + (distance - first) // dial_size


def parse_moves(path: str, dial_size: int = DIAL_SIZE, start: int = DIAL_START) -> int:
    zero_count = 0
    position = start

    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            direction = line[0]
            distance = int(line[1:])

            zero_count += count_zero_hits(position, direction, distance, dial_size)

            if direction == "R":
                position = (position + distance) % dial_size
            elif direction == "L":
                position = (position - distance) % dial_size
            else:
                raise ValueError(f"Unknown direction: {direction!r}")

    return zero_count


if __name__ == "__main__":
    result = parse_moves(PATH)
    print(f"number of 0's: {result}")