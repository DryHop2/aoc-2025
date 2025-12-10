PATH = "./inputs/day10.txt"

from collections import deque
from fractions import Fraction
import re


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


def min_presses_joltage(line: str) -> int:
    targets_match = re.search(r'\{([\d,]+)\}', line)
    if not targets_match:
        raise ValueError(f"Could not find targets in line: {line!r}")
    targets = [int(x) for x in targets_match.group(1).split(',')]
    num_counters = len(targets)
    
    buttons_raw = re.findall(r'\(([\d,]+)\)', line)
    buttons: list[list[Fraction]] = []
    for b in buttons_raw:
        indices = [int(x) for x in b.split(',')]
        col = [Fraction(0)] * num_counters
        for idx in indices:
            if idx < num_counters:
                col[idx] = Fraction(1)
        buttons.append(col)
        
    num_buttons = len(buttons)

    button_bounds: list[int | float] = []
    for b_idx in range(num_buttons):
        limit: int | float = float('inf')
        affects_something = False
        for r_idx in range(num_counters):
            if buttons[b_idx][r_idx] > 0:
                affects_something = True
                limit = min(limit, targets[r_idx])
        if not affects_something:
            limit = 0
        button_bounds.append(limit)

    matrix: list[list[Fraction]] = []
    for r in range(num_counters):
        row = [buttons[c][r] for c in range(num_buttons)]
        row.append(Fraction(targets[r]))
        matrix.append(row)

    pivot_row = 0
    pivots: dict[int, int] = {}
    
    for col in range(num_buttons):
        if pivot_row >= num_counters:
            break
   
        curr = pivot_row
        while curr < num_counters and matrix[curr][col] == 0:
            curr += 1
            
        if curr == num_counters:
            continue  

        matrix[pivot_row], matrix[curr] = matrix[curr], matrix[pivot_row]
        
        pivot_val = matrix[pivot_row][col]
        pivots[col] = pivot_row
        for c in range(col, num_buttons + 1):
            matrix[pivot_row][c] /= pivot_val

        for r in range(num_counters):
            if r != pivot_row:
                factor = matrix[r][col]
                for c in range(col, num_buttons + 1):
                    matrix[r][c] -= factor * matrix[pivot_row][c]
        
        pivot_row += 1

    free_vars = [c for c in range(num_buttons) if c not in pivots]
    pivot_vars = [c for c in range(num_buttons) if c in pivots]

    pivot_eqs: dict[int, tuple[Fraction, list[tuple[Fraction, int]]]] = {}
    for p in pivot_vars:
        row = pivots[p]
        constant = matrix[row][-1]
        dependencies: list[tuple[Fraction, int]] = []
        for f in free_vars:
            if f > p and matrix[row][f] != 0:
                dependencies.append((matrix[row][f], f))
        pivot_eqs[p] = (constant, dependencies)

    for r in range(pivot_row, num_counters):
        if matrix[r][-1] != 0:
            raise ValueError("No valid solution - inconsistent system")

    best_total: float = float('inf')
    found_solution = False

    def recursive_search(free_idx: int, current_presses: list[Fraction]) -> None:
        nonlocal best_total, found_solution

        if free_idx == len(free_vars):
            for p in pivot_vars:
                constant, deps = pivot_eqs[p]
                val = constant
                for coeff, f_col in deps:
                    val -= coeff * current_presses[f_col]
                
                if val < 0 or val.denominator != 1:
                    return
                if val > button_bounds[p]:
                    return
                    
                current_presses[p] = val

            current_total = sum(current_presses)
            if current_total < best_total:
                best_total = current_total
                found_solution = True
            return

        f_col = free_vars[free_idx]
        limit = button_bounds[f_col]
        
        for val in range(int(limit) + 1):
            current_presses[f_col] = Fraction(val)

            possible = True
            for p in pivot_vars:
                constant, deps = pivot_eqs[p]
                current_val = constant
                depends_on_future = False
                
                for coeff, dep_f in deps:
                    if dep_f == f_col or dep_f in free_vars[:free_idx]:
                        current_val -= coeff * current_presses[dep_f]
                    else:
                        depends_on_future = True
                
                if not depends_on_future:
                    if current_val < 0 or current_val.denominator != 1:
                        possible = False
                        break

            if possible:
                recursive_search(free_idx + 1, current_presses)

    initial_presses = [Fraction(0)] * num_buttons
    recursive_search(0, initial_presses)

    if not found_solution:
        raise ValueError("No valid solution")

    return int(best_total)


def part2(text: str) -> int:
    total = 0
    for line in text.strip().splitlines():
        total += min_presses_joltage(line)
    return total


def main(path: str = PATH):
    with open(path) as f:
        data = f.read()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()