from functools import lru_cache


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


def count_paths_dp(graph, start, goal):
    @lru_cache(maxsize=None)
    def dfs(node):
        if node == goal:
            return 1
        return sum(dfs(nei) for nei in graph.get(node, []))
    return dfs(start)


def count_paths_dac_fft_dp(graph, start, goal):
    @lru_cache(maxsize=None)
    def dfs(node, seen_dac, seen_fft):
        if node == "dac":
            seen_dac = True
        if node == "fft":
            seen_fft = True
        if node == goal:
            return 1 if (seen_dac and seen_fft) else 0
        return sum(dfs(nei, seen_dac, seen_fft) for nei in graph.get(node, []))
    return dfs(start, False, False)


def main(path: str = PATH):
    with open(path, "r") as f:
        graph = parse(f)
    print(count_paths(graph, "you", "out"))
    print(count_paths_dac_fft_dp(graph, "svr", "out"))
    

if __name__ == "__main__":
    main()