PATH = "./inputs/day11.txt"


def parse(lines):
    graph = {}
    for line in lines:
        name, rhs = line.split(":")
        name = name.strip()
        targets = rhs.split()
        graph[name] = targets
    
    return graph


def count_paths(graph, start, goal):
    count = 0
    stack = [(start, {start})]

    while stack:
        node, visited = stack.pop()

        if node == goal:
            count += 1
            continue

        for neighbor in graph.get(node, []):
            if neighbor in visited:
                continue
            new_visited = visited | {neighbor}
            stack.append((neighbor, new_visited))

    return count


def main(path: str = PATH):
    with open(path, "r") as f:
        graph = parse(f)
    print(count_paths(graph, "you", "out"))
    

if __name__ == "__main__":
    main()