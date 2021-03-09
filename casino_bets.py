# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, K):
    """
    >>> solution(10, 10)
    4
    >>> solution(18, 2)
    6
    >>> solution(18, 5)
    5
    >>> solution(8, 0)
    7
    >>> solution(1, 0)
    0
    >>> solution(2, 0)
    1

    >>> solution(2, 2_000_000_000)
    1
    """

    # not really sure what to return if N=1, it should be invalid?
    rounds = N - 1
    next_num = N
    while K > 0 and next_num >= 4:
        next_num = next_num - next_num % 2
        next_num = next_num // 2
        rounds -= (next_num - 1)
        K -= 1
    return rounds
