from typing import List


test_numbers = [0]


def load_from_files():
    test_arr = []
    for t in test_numbers:
        with open(f"dynamic_arrays_t{t}.txt", "r") as ptr:
            line = ptr.readline()
            n = int(line.split()[0])
            test_lines = []
            for line in ptr:
                if line == '\n':
                    break
                test_line = list(map(int, line.split()))
                if len(test_line) != 3:
                    assert False
                assert len(test_line) == 3, f"invalid line: {line}"
                test_lines.append(test_line)
            expected = list(map(int, ptr))
            test_arr.append((n, test_lines, expected))
    return test_arr


tests = load_from_files()


def dynamicArray(n: int, queries: List[List[int]]):
    """
    >>> dynamicArray(2, [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]])
    [7, 3]
    >>> dynamicArray(tests[0][0], tests[0[1]]) == tests[0][2]
    True
    """
    arr = [[] for _ in range(n)]
    ret_arr = []
    last_answer = 0
    for q in queries:
        query_type, x, y = q
        idx = (x ^ last_answer) % n
        sub_arr = arr[idx]
        if query_type == 1:
            sub_arr.append(y)
        else:
            idx2 = y % len(sub_arr)
            last_answer = sub_arr[idx2]
            ret_arr.append(last_answer)
    return ret_arr



