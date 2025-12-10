PATH = "./inputs/day10.txt"


from collections import deque


def min_presses(target: int, buttons: list[int]) -> int | None:
    if target == 0:
        return 0
    
    start = 0
    visited = {start}
    q = deque([(start, 0)])

    while q:
        state, presses = q.popleft()

        for b in buttons:
            new_state = state ^ b
            if new_state == target:
                return presses + 1
            if new_state not in visited:
                visited.add(new_state)
                q.append((new_state, presses + 1))

    return None


def parse_line(line: str):
    tokens = line.split()
    pattern_token = tokens[0]
    pattern = pattern_token.strip("[]")
    num_lights = len(pattern)

    target_mask = 0
    for i, ch in enumerate(pattern):
        if ch == "#":
            target_mask |= (1 << i)

    button_masks = []
    for tok in tokens[1:]:
        if tok.startswith("("):
            inner = tok.strip("()")
            if not inner:
                continue
            indices = [int(x) for x in inner.split(",")]
            mask = 0
            for idx in indices:
                mask |= (1 << idx)
            button_masks.append(mask)

    return target_mask, button_masks


def part1(text: str) -> int:
    total_presses = 0
    for line in text.strip().splitlines():
        target, buttons = parse_line(line)
        presses = min_presses(target, buttons)
        if presses is None:
            raise ValueError("Unreachable")
        total_presses += presses
    
    return total_presses


def main(path: str = PATH):
    with open(path) as f:
        data = f.read()
    print(part1(data))


if __name__ == "__main__":
    main()