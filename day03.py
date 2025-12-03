PATH = "./inputs/day03.txt"


def max_joltage_for_bank(bank: str) -> int:
    bank = bank.strip()
    max_first = int(bank[0])
    best = -1

    for ch in bank[1:]:
        d = int(ch)
        candidate = 10 * max_first + d
        if candidate > best:
            best = candidate

        if d > max_first:
            max_first = d

    return best


def total_output(path: str) -> int:
    total = 0
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            total += max_joltage_for_bank(line)

    return total


if __name__ == "__main__":
    result = total_output(PATH)
    print(result)