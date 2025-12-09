PATH = "./inputs/day09.txt"


from collections import deque


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

            # if x1 == x2 or y1 == y2:
            #     continue

            width = abs(x2 - x1) + 1
            length = abs(y2 - y1) + 1
            area = width * length

            if area > max_area:
                max_area = area

    return max_area


def build_allowed(points):
    red_set = set(points)
    boundary = set(red_set)
    n = len(points)

    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]

        if x1 == x2:
            y_lo, y_hi = sorted((y1, y2))
            for y in range(y_lo, y_hi + 1):
                boundary.add((x1, y))
        elif y1 == y2:
            x_lo, x_hi = sorted((x1, x2))
            for x in range(x_lo, x_hi + 1):
                boundary.add((x, y1))
        else:
            raise ValueError("Adjacent red tiles must share row or column")
        
    xs = [x for x, _ in points]
    ys = [y for _, y in points]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)

    outside = set()
    start = (xmin - 1, ymin - 1)
    outside.add(start)
    q = deque([start])


    def neighbors(x, y):
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if nx < xmin - 1 or nx > xmax + 1 or ny < ymin - 1 or ny > ymax + 1:
                continue
            
            yield nx, ny

    print("xmin,xmax,dx =", xmin, xmax, xmax - xmin)
    print("ymin,ymax,dy =", ymin, ymax, ymax - ymin)



    while q:
        x, y = q.popleft()
        for nx, ny in neighbors(x, y):
            if (nx, ny) in outside:
                continue
            if (nx, ny) in boundary:
                continue
            outside.add((nx, ny))
            q.append((nx, ny))

    interior = set()
    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            if (x, y) in boundary:
                continue
            if (x, y) in outside:
                continue
            interior.add((x, y))

    allowed = boundary | interior
    return allowed, red_set


def part2(text: str) -> int:
    points = parse(text)
    allowed, red_set = build_allowed(points)

    reds = list(red_set)
    n = len(reds)
    max_area = 0

    for i in range(n):
        x1, y1 = reds[i]
        for j in range(i + 1, n):
            x2, y2 = reds[j]

            min_x, max_x = sorted((x1, x2))
            min_y, max_y = sorted((y1, y2))

            width = max_x - min_x + 1
            length = max_y - min_y + 1
            area = length * width

            if area <= max_area:
                continue

            ok = True
            for x in range(min_x, max_x + 1):
                for y in range(min_y, max_y + 1):
                    if (x, y) not in allowed:
                        ok = False
                        break
                if not ok:
                    break

            if ok:
                max_area = area

    return max_area


def main(path: str = PATH):
    with open(path, "r") as f:
        data = f.read()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()