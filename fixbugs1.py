def solution(M, A):
    '''

    :param M:
    :param A:
    :return:

    >>> solution(2, [1, 2])
    1
    >>> solution(2, [1, 2, 2, 2])
    2
    >>> solution(2, [1, 1, 2, 2, 2, 1, 1])
    1
    >>> solution(2, [2, 2, 2])
    2
    >>> solution(2, [0, 0, 1, 2])
    0
    >>> solution(3, [1,2,3,3,1,3,1])
    3
    >>> solution(2, [1,1,2])
    1
    '''
    N = len(A)
    count = [0] * (M + 1)
    maxOccurence = 1
    index = 0
    for i in range(N):
        if count[A[i]] > 0:
            tmp = count[A[i]] + 1
            if tmp > maxOccurence:
                maxOccurence = tmp
                index = i
            count[A[i]] = tmp
        else:
            count[A[i]] = 1
    return A[index]