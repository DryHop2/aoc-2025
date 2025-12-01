DIAL_SIZE = 100
DIAL_START = 50

zero_count = 0
position = DIAL_START


def count_zero_hits(position: int, direction: str, distance: int, dial_size: int = 100) -> int:
    if distance <= 0:
        return 0
    
    if direction == "R":
        first = dial_size if position == 0 else dial_size - position
    elif direction == "L":
        first = dial_size if position == 0 else position

    if distance < first:
        return 0
    
    return 1 + (distance - first) // dial_size


with open("./inputs/day01.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        direction = line[0]
        distance = int(line[1:])

        zero_count += count_zero_hits(position, direction, distance, DIAL_SIZE)

        if direction == "R":
            position = (position + distance) % DIAL_SIZE
        elif direction == "L":
            position = (position - distance) % DIAL_SIZE

print(f"number of 0's: {zero_count}")