import heapq
from math import prod


PATH = "./inputs/day08.txt"


def parse(text: str):
    points = []
    for line in text.strip().splitlines():
        x, y, z = map(int, line.split(","))
        points.append((x, y, z))
    return points


def build_edges(points):
    n = len(points)
    edges = []
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2
            dist2 = dx*dx + dy*dy + dz*dz
            edges.append((dist2, i, j))
    edges.sort(key=lambda e: e[0])

    return edges


def part1(text: str, num_pairs: int = 1000):
    points = parse(text)
    n = len(points)


    def gen_edges():
        for i in range(n):
            x1, y1, z1 = points[i]
            for j in range(i + 1, n):
                x2, y2, z2 = points[j]
                dx = x1 - x2
                dy = y1 - y2
                dz = z1 - z2
                dist2 = dx*dx + dy*dy + dz*dz
                yield (dist2, i, j)


    edges = heapq.nsmallest(num_pairs, gen_edges(), key=lambda e: e[0])

    parent = list(range(n))
    size = [1] * n


    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        
        return x
    

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]


    for _, i, j in edges:
        union(i, j)

    comps = {}
    for i in range(n):
        root = find(i)
        comps[root] = comps.get(root, 0) + 1

    sizes = sorted(comps.values(), reverse=True)

    return prod(sizes[:3])


def part2(text: str):
    points = parse(text)
    n = len(points)
    edges = build_edges(points)

    parent = list(range(n))
    size = [1] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]

        return x
    

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return False
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]

        return True
    

    components = n
    last_pair = None
    

    for _, i, j in edges:
        if union(i, j):
            components -= 1
            last_pair = (i, j)
            if components == 1:
                break

    if last_pair is None:
        raise RuntimeError("Graph never fully connected")
    
    i, j = last_pair
    x1 = points[i][0]
    x2 = points[j][0]
    
    return x1 * x2


def main(path: str = PATH):
    with open(path, "r") as f:
        data = f.read()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()