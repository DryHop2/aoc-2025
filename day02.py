PATH = "./inputs/day02.txt"


# def is_invalid_pid(n: int) -> bool:
#     s = str(n)
#     if len(s) % 2 != 0:
#         return False
    
#     midpoint = len(s) // 2
#     return s[:midpoint] == s[midpoint:]


def is_invalid_pid(n: int) -> bool:
    s = str(n)
    L = len(s)
    if L < 2:
        return False
    
    for chunk_len in range(1, L // 2 + 1):
        if L % chunk_len != 0:
            continue

        repeats = L // chunk_len
        if repeats < 2:
            continue

        chunk = s[:chunk_len]
        if chunk * repeats == s:
            return True
    
    return False


def sum_invalid_pids(path: str = PATH) -> int:
    with open(path, "r") as f:
        line = f.read().strip()

    result = 0

    for pid_range in line.split(","):
        start_str, end_str = pid_range.split("-")
        start = int(start_str)
        end = int(end_str)

        for n in range(start, end + 1):
            if is_invalid_pid(n):
                result += n

    return result


if __name__ == "__main__":
    result = sum_invalid_pids(PATH)
    print(result)