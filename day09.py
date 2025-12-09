PATH = "./inputs/day09.txt"


def parse(text: str):
    points = []
    for line in text.strip().splitlines():
        x, y = map(int, line.split(","))
        points.append((x, y))
    
    return points


def part1(text: str) -> int:
    points = parse(text)
    n = len(points)
    max_area = 0

    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]

            if x1 == x2 or y1 == y2:
                continue

            width = abs(x2 - x1) + 1
            length = abs(y2 - y1) + 1
            area = width * length

            if area > max_area:
                max_area = area

    return max_area


def main(path: str = PATH):
    with open(path, "r") as f:
        data = f.read()

    print(part1(data))


if __name__ == "__main__":
    main()