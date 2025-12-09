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

            # if x1 == x2 or y1 == y2:
            #     continue

            width = abs(x2 - x1) + 1
            length = abs(y2 - y1) + 1
            area = width * length

            if area > max_area:
                max_area = area

    return max_area


def part2(text: str) -> int:
    points = parse(text)
    red_set = set(points)
    n = len(points)
    edges = []

    for i in range(n):
        p1 = points[i]
        p2 = points[(i + 1) % n]
        edges.append((p1, p2))

    def point_inside_or_boundary(px, py):
        for (x1, y1), (x2, y2) in edges:
            if x1 == x2 == px:
                if min(y1, y2) <= py <= max(y1, y2):
                    return True
            elif y1 == y2 == py:
                if min(x1, x2) <= px <= max(x1, x2):
                    return True
                
        crossings = 0
        for (x1, y1), (x2, y2) in edges:
            if y1 == y2:
                continue
            if x1 == x2:
                if x1 > px:
                    y_lo, y_hi = min(y1, y2), max(y1, y2)
                    if y_lo <= py < y_hi:
                        crossings += 1
        
        return crossings % 2 == 1
    

    def rectangle_valid(min_x, max_x, min_y, max_y):
        corners = [(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)]
        for cx, cy in corners:
            if not point_inside_or_boundary(cx, cy):
                return False
            
        for (x1, y1), (x2, y2) in edges:
            if x1 == x2:
                if min_x < x1 < max_x:
                    y_lo, y_hi = min(y1, y2), max(y1, y2)
                    if y_lo < max_y and y_hi > min_y:
                        return False
            else:
                if min_y < y1 < max_y:
                    x_lo, x_hi = min(x1, x2), max(x1, x2)
                    if x_lo < max_x and x_hi > min_x:
                        return False
        
        return True
    

    reds = list(red_set)
    num_reds = len(reds)
    max_area = 0

    for i in range(num_reds):
        x1, y1 = reds[i]
        for j in range(i + 1, num_reds):
            x2, y2 = reds[j]

            min_x, max_x = min(x1, x2), max(x1, x2)
            min_y, max_y = min(y1, y2), max(y1, y2)

            area = (max_x - min_x + 1) * (max_y - min_y + 1)

            if area <= max_area:
                continue
            if rectangle_valid(min_x, max_x, min_y, max_y):
                max_area = area

    return max_area


def main(path: str = PATH):
    with open(path, "r") as f:
        data = f.read()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()


# This is still slow as hell but at least gets an answer. Find a better way.
# Lol. The answer is wrong.
# stupid typo